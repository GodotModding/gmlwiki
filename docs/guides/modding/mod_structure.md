---
description: Mod file structure is a small but important part of modding.
---

# Mod Structure

Mod file structure is a small but important part of modding. If your files are in the wrong place, they won't be found 
by the mod loader and can't work correctly.

There are two main types of folders where mods are loaded from - one loads packed and the other unpacked mods. Packed in
case of this mod loader just means "it is a ZIP", since that's how our mods are distributed. Unpacked is the raw mod code
which you can easily edit within the editor. Editor and ZIP require slightly different structures you can see below.

!!! tip
    It's good to know about the general structure, if just to know what you can and can't change - but if you don't 
    want to set everything up manually, you can use the [Mod Tool](tools/mod_tool.md) to set your new mod project up and 
    export everything correctly - including all asset imports no matter the name.

## Editor
When developing mods for the Godot Mod Loader, everything is done within the `res://mods-unpacked` folder. You will place
your own mod folder here when working on it. Mod folder names must follow the convention of `{Namespace}-{ModName}`, which 
is also your mod's ID. Using this schema avoids collision with other mod ids, and also allows them to be compatible with 
Thunderstore. A mod folder always contains these important files:
```
res://
└───mods-unpacked
    └───Author-ModName
        ├───mod_main.gd
        └───manifest.json
```
*See [Mod Files](mod_files.md) for info on what those files do.*

!!! warning 
    If you have any dependencies, you need while developing your mod, unzip them and place them in `res://mods-unpacked`.
    A bug in the Godot editor (any version before [4.4](https://github.com/godotengine/godot/pull/90425)) prevents 
    using zipped and unpacked mods at the same time (see [ZIPs in the Editor](#zips-in-the-editor) below).

## ZIPs
Mod ZIPs should have the structure shown below. It matches the structure of the filesystem when developing mods in the 
Godot editor. Yes, the zip itself contains the `/mods-unpacked` folder - this has to be this way because of how Godot 
loads resource packs into the project root directly. 

Mod users will add their ZIPs to a folder named `/mods` in the root of the project, which is `res://` or next to the game executable.

ZIP names must follow the convention of `{Namespace}-{ModName}-{version}.zip` e.g. `GodotModding-CoolMod-1.2.3.zip`.

=== "Godot 4"

    ```
    Author-ModName-1.2.3.zip/
    ├── .godot/
    │   └── imported/
    │       └── icon.stex
    └── mods-unpacked/
        └── Author-ModName/
            ├── mod_main.gd
            ├── manifest.json
            ├── overwrites.gd
            ├── extensions/
            │   └── main.gd
            └── overwrites/
                └── icon.png
    ```

=== "Godot 3"

    ```
    Author-ModName-1.2.3.zip/
    ├── .import/
    │   └── icon.stex
    └── mods-unpacked/
        └── Author-ModName/
            ├── mod_main.gd
            ├── manifest.json
            ├── overwrites.gd
            ├── extensions/
            │   └── main.gd
            └── overwrites/
                └── icon.png
    ```

Mod ZIPs need to include any custom assets from the [import folder](#the-import-folder), otherwise Godot won't know they exist.

Your mod ZIP's import folder **should only include your custom assets**. It should __**not**__ include any vanilla assets.

### ZIPs in the Editor
Godot has a bug that, in short, means you can't use both unpacked mods (in res://mods-unpacked) and zipped mods 
(in res://mods) in the Editor - [until 4.4](https://github.com/godotengine/godot/pull/90425). If you need to use another
mod as a dependency, you can unzip it and place it with your mod into `res://mods-unpacked/`.

You can still use mod ZIPs in the editor, when testing your zipped mod for example. 
They will load as expected, but nothing from `res://mods-unpacked` will be loaded.

## The import folder

=== "Godot 4"

      Godot projects save a version of custom assets, such as PNGs, to a folder within the godot data folder:
      `res://.godot/imported/` (e.g. PNGs are saved as *.godot/imported/filename.[stex](https://docs.godotengine.org/en/stable/classes/class_streamtexture.html)*). 
      Assets are streamed from the files in this folder, rather than from the asset in the file system.

=== "Godot 3"

      Godot projects save a version of custom assets, such as PNGs, to a top-level folder:
      `res://.import` (e.g. PNGs are saved as *.import/filename.[stex](https://docs.godotengine.org/en/stable/classes/class_streamtexture.html)*). 
      Assets are streamed from the files in this folder, rather than from the asset in the file system.

### Tips
It's highly recommended that you prefix all custom assets with `modname_*`, e.g. `modname_weapon1.png`. 
This makes it much easier to find your custom assets in the import folder, when building the mod ZIP or adding 
files to a mod's repo.

If you move assets around in the filesystem, Godot won't remove the old files from `.import`, which can make it bloated 
with unused, unreferenced files. To clean up these unused files, delete everything in the import folder and run the game again. 
This will re-create only the files that are actually used.

Custom assets can usually also be identified by sorting by creation date.

### Notes
If you want to rename existing assets to include a `modname_*` prefix (as per [Tips](#tips) above), you'll need to do two things:
1. Rename the files themselves.
    - Windows has a "PowerToy" ([download](https://learn.microsoft.com/en-us/windows/powertoys/)/[repo](https://learn.microsoft.com/en-us/windows/powertoys/)) called [Power Rename](https://learn.microsoft.com/en-us/windows/powertoys/powerrename) that will let you do this quickly, and it [supports regex](https://learn.microsoft.com/en-us/windows/powertoys/powerrename#regular-expressions).
    - To rename with Power Rename:
        - Enable the "Use regular expressions" option
        - Search string: `([A-z0-9_!-]+).png`
        - Replace string: `modname_$1.png`
2. Update the resource paths.
    - You can use VS Code to do this, as its search and replace also supports regex.

For (2), here's some example regex to replace PNG filenames in .tres files. It supports these characters in file and folder names: `A-z`, `0-9`, and `_`. See what it's doing on [regex101.com](https://regex101.com/r/lJscaf/1).

Search:
```regex
\[ext_resource path="res:\/\/mods-unpacked\/AuthorName-ModName\/([A-z0-9_!-\/]+)\/([A-z0-9_!-]+).png
```

Replace:
```gdscript2
[ext_resource path="res://mods-unpacked/AuthorName-ModName/$1/modname_$2.png
```

---

