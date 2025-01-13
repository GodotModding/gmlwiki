# Mod Structure
## Editor
When developing mods in Godot, create a folder named mods-unpacked and add your mods there.

Mod folder names must follow the convention of `{AuthorName}-{ModName}`:
```
res://
└───mods-unpacked
    └───Author-ModName
        ├───mod_main.gd
        └───manifest.json
```
*See [Mod Files](mod_files.md) for info on what those files do.*

If you have any dependencies, unzip them and add them to res://mods-unpacked.

???+ note 
     A bug in the Godot editor prevents using zipped and unpacked mods at the same time (see [ZIPs in the Editor](#zips-in-the-editor) below).

## ZIPs
Mod ZIPs should have the structure shown below. The structure matches the structure of the filesystem when developing mods in the Godot editor.

Mod users will add their ZIPs to a folder named mods in the root.

ZIP names must follow the convention of `namespace-modname-version.zip` e.g. `GodotModding-CoolMod-1.2.3.zip`.

=== "Godot 4"

    ```
    Author-ModName-1.2.3.zip/
    ├── .godot/
    │   └── imported
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

### ZIPs in the Editor
Godot has a bug that, in short, means you can't use both unpacked mods (in res://mods-unpacked) and zipped mods (in res://mods) in the Editor. If you need to use a mod as a dependency, please unzip it and add it to your project.

You can still use mod ZIPs in the editor, eg. if you want to test your zipped mod. They will load as expected, but nothing from res://mods-unpacked will be loaded either.

## .import
Godot projects save a version of custom assets, such as PNGs, to a top-level directory called .import (eg. PNGs are saved as *.import/filename.[stex](https://docs.godotengine.org/en/stable/classes/class_streamtexture.html)*). Assets are streamed from the files in this folder, rather than from the asset in the file system.

### Distribution
Mod ZIPs need to include any custom assets from the .import folder.

Like in the editor, these go in a top-level directory called .import in your ZIP.

Your mod ZIP's .import folder **should only include your custom assets**. It should __**not**__ include any vanilla assets.

### Tips
It's highly recommended that you prefix all custom assets with your `modname_*`, eg `modname_weapon1.png`. This makes it much easier to find your custom assets in *.import*, when building your mod ZIP or adding files to a mod's repo.

If you move assets around in the filesystem, Godot won't remove the old files from `.import`, which can make it bloated with unused, unreferenced files. To clean up these unused files, delete everything in .import and run the game again. This will re-create only the files that are actually used.

Custom assets can also be identified by sorting by date.

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
```gdscript
[ext_resource path="res://mods-unpacked/AuthorName-ModName/$1/modname_$2.png
```

---

