# Adding and Replacing Game Resources

With the Godot alone it's possible to replace/overwrite existing game resources, and add resources in specific places in
the project. With the Mod Loader, we use a specific convention to both make the process more organized and to apply
overwrites at the correct point in the game startup.

The system described below can also be used to place assets from your mod folder in specific locations in the game's 
file system without messing with your [mod structure](mod_structure.md). Some games require this - Dome Keeper, for 
example, loads all upgrade icons from one folder. The code assumes even modded assets to be there when creating new upgrades.

## overwrites.gd
The `overwrites.gd` file is used to define resource overwrites in a separate file. In general, any file in a project 
can be overwritten, but we highly recommend that you only use this feature for images, audio and other types that 
inherit from `Resource`.

We recommend the following directory structure for your overwrites:
```
res://
└───mods-unpacked/
    └───Author-ModName/
        ├───mod_main.gd
        ├───manifest.json
        ├───overwrites.gd
        └───overwrites/
            └───original_dir_name/
                └───original_file_name.png
```

The following steps are required to create an overwrite:

1. Open the file you want to replace by right-clicking and selecting *Open in File Manager*.
2. Create a replacement file that matches the metadata of the original file 1:1. For example, for images, make sure 
   that the resolution is the same.
3. Add the replacement file to the overwrites directory. Ideally, structure your overwrites as shown above.
4. Add the required code to `overwrites.gd`.

???+ Tip
    Creating overwrites be done quickly by using the [Mod Tool file context menu](tools/mod_tool.md#file-system-context-menu)

## Example
##### Using `preload`
```gdscript
extends Node

func _init():
    var overwrite_0 = preload("res://mods-unpacked/Author-ModName/overwrites/assets/images/GodotModded.png")
    overwrite_0.take_over_path("res://assets/images/GodotModded.png")
```

##### Using `load`
Load only works if the overwrite goes into script scope (as opposed to staying in function scope) at some point, 
otherwise Godot won't be able to find the file. No idea why. There are two ways to do this: a global variable 
declaration or a global Array to which the overwrites are appended. The global variable only works for a single 
overwrite, so this example uses the Array.

=== "Godot 4"

    ```gdscript
    extends Node
    
    var icons: Array # this declaration NEEDS to have script scope
    const ICONS := [
        "GodotModded.png",
        "UpgradeIcon.png"
    ]
    var mod_icons_folder := "res://mods-unpacked/Author-ModName/overwrites/assets/icons"
    var vanilla_icons_folder := "res://assets/icons"
    
    func _init():
        # var icons: Array # this would not work
        for image in ICONS:
            var icon_overwrite := load(mod_icons_folder.path_join(image))
            icon_overwrite.take_over_path(vanilla_icons_folder.path_join(image))
            icons.append(icon_overwrite)  # this essentially pulls the overwrite into global scope
    ```

=== "Godot 3"

    ```gdscript
    extends Node
    
    var icons: Array # this declaration NEEDS to have script scope
    const ICONS := [
        "GodotModded.png",
        "UpgradeIcon.png"
    ]
    var mod_icons_folder := "res://mods-unpacked/Author-ModName/overwrites/assets/icons"
    var vanilla_icons_folder := "res://assets/icons"
    
    func _init():
        # var icons: Array # this would not work
        for image in ICONS:
            var icon_overwrite := load(mod_icons_folder.plus_file(image))
            icon_overwrite.take_over_path(vanilla_icons_folder.plus_file(image))
            icons.append(icon_overwrite)  # this essentially pulls the overwrite into global scope
    ```
```
Instead of using an array of Strings here, you could also use the [Directory](https://docs.godotengine.org/en/3.5/classes/class_directory.html) class to go over each file in a 
folder and create and overwrite with it.
