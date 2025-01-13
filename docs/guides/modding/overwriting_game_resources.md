# Adding and Replacing Game Resources
## overwrites.gd
The `overwrites.gd` file is used to define resource overwrites in a separate file. In general, any file in a project 
can be overwritten, but we highly recommend that you only use this feature for images, audio and other types that 
inherit from `Resource`.

We recommend the following directory structure for your overwrites:
```
res://
└───mods-unpacked
    └───Author-ModName
        ├───mod_main.gd
        ├───manifest.json
        ├───overwrites.gd
        └───overwrites
            └───original_dir_name
                └───original_file_name.png
```

The following steps are required to create an overwrite:

1. Open the file you want to replace by right-clicking and selecting *Open in File Manager*.
2. Create a replacement file that matches the metadata of the original file 1:1. For example, for images, make sure that the resolution is the same.
3. Add the replacement file to the overwrites directory. Ideally, structure your overwrites as shown above.
4. Add the required code to `overwrites.gd`.

## Example
##### Using `preload`
```gdscript
extends Node

func _init():
    var overwrite_0 = preload("res://mods-unpacked/Author-ModName/overwrites/assets/images/GodotModded.png")
    overwrite_0.take_over_path("res://assets/images/GodotModded.png")
```

##### Using `load`
Load only works if the overwrite goes into script scope (as opposed to staying in funtion scope) at some point, 
otherwise Godot won't be able to find the file. No idea why. There are two ways to do this: a global variable 
declaration or a global Array to which the overwrites are appended. The global variable only works for a single 
overwrite, so this example uses the Array.
```gdscript
extends Node

var icons: Array # this declaration NEEDS to have script scope
const ICONS := [
    "GodotModded.png",
    "UpgradeIcon.png"
]

func _init():
    # var icons: Array # this would not work
    for image in ICONS:
        var icon_overwrite := load("res://mods-unpacked/Author-ModName/overwrites/assets/icons".plus_file(image))
        icon_overwrite.take_over_path("res://assets/icons".plus_file(image))
        icons.append(icon_overwrite)  # this essentially pulls the overwrite into global scope
```
Instead of using an array of Strings here, you could also use the [Directory](https://docs.godotengine.org/en/3.5/classes/class_directory.html) class to go over each file in a folder and create and overwrite with it.


## Mod Tool
You can use [Mod Tool](tools/mod_tool.md) to make overwriting assets easier. If you have the plugin activated:
*right-click -> ModTool: Create Asset Overwrite* on the asset you want to replace