---
status: new
description: This Class provides helper functions to build mods.
---

# ModLoaderMod
**Inherits**: Object


This Class provides helper functions to build mods.
<hr style="border-width: thick">

## Constants
#### • `#!gd2 LOG_NAME`: `#!gd2 "ModLoader:Mod"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 

<hr style="border-width: thick">

## Method Descriptions
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 install_script_extension(` `#!gd2 child_script_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-install_script_extension data-toc-label='install_script_extension' .no-code-padding}
#### Description:
Installs a script extension that extends a vanilla script.

#### Parameters:
  
- `#!gd2 child_script_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the mod's extender script.

**Returns:**
  
- No return value

This is the preferred way of modifying a vanilla [`#!gd2 Script`](https://docs.godotengine.org/en/stable/classes/class_script.html)  
Since Godot 4, extensions can cause issues with scripts that use `#!gd2 class_name` and should be avoided if present.  
See [`#!gd2 add_hook()`](#method-add_hook) for those cases.

The `#!gd2 child_script_path` should point to your mod's extender script.  
Example: `#!gd2 "MOD/extensions/singletons/utils.gd"`  
Inside the extender script, include `#!gd2 extends {target}` where `#!gd2 {target}` is the vanilla path.  
Example: `#!gd2 extends "res://singletons/utils.gd"`.  


!!! note 
	Your extender script doesn't have to follow the same directory path as the vanilla file, but it's good practice to do so.



***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 install_script_hooks(` `#!gd2 vanilla_script_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 hook_script_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-install_script_hooks data-toc-label='install_script_hooks' .no-code-padding}
#### Description:
Adds all methods from a file as hooks. 

#### Parameters:
  
- `#!gd2 vanilla_script_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the script which will be hooked.  
- `#!gd2 hook_script_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the script containing hooks.

**Returns:**
  
- No return value

The file needs to extend [`#!gd2 Object`](https://docs.godotengine.org/en/stable/classes/class_object.html).  
The methods in the file need to have the exact same name as the vanilla method they intend to hook, all mismatches will be ignored.   
See: [`#!gd2 add_hook()`](#method-add_hook)   
#### Examples:
  

```gdscript2 
ModLoaderMod.install_script_hooks(
    "res://tools/utilities.gd",
    extensions_dir_path.path_join("tools/utilities-hook.gd")
)
```
***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 add_hook(` `#!gd2 mod_callable:`&nbsp;&nbsp;[`#!gd2 Callable`](https://docs.godotengine.org/en/stable/classes/class_callable.html)`#!gd2 , ` `#!gd2 script_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 method_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-add_hook data-toc-label='add_hook' .no-code-padding}
#### Description:
Adds a hook, a custom mod function, to a vanilla method.

#### Parameters:
  
- `#!gd2 mod_callable` ([`#!gd2 Callable`](https://docs.godotengine.org/en/stable/classes/class_callable.html)): The function that will executed when the vanilla method is executed. When writing a mod callable, make sure that it *always* receives a [`#!gd2 ModLoaderHookChain`](mod_loader_hook_chain.md) object as first argument, which is used to continue down the hook chain (see: [`#!gd2 ModLoaderHookChain.execute_next()`](mod_loader_hook_chain.md#method-execute_next)) and allows manipulating parameters before and return values after the vanilla method is called.   
- `#!gd2 script_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): Path to the vanilla script that holds the method.  
- `#!gd2 method_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The method the hook will be applied to.

**Returns:**


- No return value

Opposed to script extensions, hooks can be applied to scripts that use `#!gd2 class_name` without issues.  
If possible, prefer [`#!gd2 install_script_extension()`](#method-install_script_extension).

#### Examples:


Given the following vanilla script `#!gd2 main.gd`
```gdscript2 
class_name MainGame
extends Node2D

var version := "vanilla 1.0.0"


func _ready():
    $CanvasLayer/Control/Label.text = "Version: %s" % version
    print(Utilities.format_date(15, 11, 2024))
```
 It can be hooked in `#!gd2 mod_main.gd` like this
```gdscript2 
func _init() -> void:
    ModLoaderMod.add_hook(change_version, "res://main.gd", "_ready")
    ModLoaderMod.add_hook(time_travel, "res://tools/utilities.gd", "format_date")
    # Multiple hooks can be added to a single method.
    ModLoaderMod.add_hook(add_season, "res://tools/utilities.gd", "format_date")


# The script we are hooking is attached to a node, which we can get from reference_object
# then we can change any variables it has
func change_version(chain: ModLoaderHookChain) -> void:
    # Using a typecast here (with "as") can help with autocomplete and avoiding errors
    var main_node := chain.reference_object as MainGame
    main_node.version = "Modloader Hooked!"
    # _ready, which we are hooking, does not have any arguments
    chain.execute_next()


# Parameters can be manipulated easily by changing what is passed into .execute_next()
# The vanilla method (Utilities.format_date) takes 3 arguments, our hook method takes
# the ModLoaderHookChain followed by the same 3
func time_travel(chain: ModLoaderHookChain, day: int, month: int, year: int) -> String:
    print("time travel!")
    year -= 100
    # Just the vanilla arguments are passed along in the same order, wrapped into an Array
    var val = chain.execute_next([day, month, year])
    return val


# The return value can be manipulated by calling the next hook (or vanilla) first
# then changing it and returning the new value.
func add_season(chain: ModLoaderHookChain, day: int, month: int, year: int) -> String:
    var output = chain.execute_next([day, month, year])
    match month:
        12, 1, 2:
            output += ", Winter"
        3, 4, 5:
            output += ", Spring"
        6, 7, 8:
            output += ", Summer"
        9, 10, 11:
            output += ", Autumn"
    return output
```
***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 register_global_classes_from_array(` `#!gd2 new_global_classes:`&nbsp;&nbsp;[`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)`#!gd2 ) static ` {#method-register_global_classes_from_array data-toc-label='register_global_classes_from_array' .no-code-padding}
#### Description:
Registers an array of classes to the global scope since Godot only does that in the editor.

#### Parameters:
  
- `#!gd2 new_global_classes` ([`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of class definitions to be registered.

**Returns:**
  
- No return value

Format: `#!gd2 { "base": "ParentClass", "class": "ClassName", "language": "GDScript", "path": "res://path/class_name.gd" }`



!!! tip 
	You can find these easily in the project.godot file under `_global_script_classes`
	(but you should only include classes belonging to your mod)
  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 add_translation(` `#!gd2 resource_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-add_translation data-toc-label='add_translation' .no-code-padding}
#### Description:
Adds a translation file.

#### Parameters:
  
- `#!gd2 resource_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the translation resource file.  
**Returns:**
  
- No return value



!!! note 
	The `#!gd2 .translation` file should have been created by the Godot editor already, usually when importing a CSV file. The translation file should named `#!gd2 name.langcode.translation` -> `#!gd2 mytranslation.en.translation`.
  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 refresh_scene(` `#!gd2 scene_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-refresh_scene data-toc-label='refresh_scene' .no-code-padding}
#### Description:
Marks the given scene for to be refreshed. It will be refreshed at the correct point in time later.

#### Parameters:
  
- `#!gd2 scene_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the scene file to be refreshed.   
**Returns:**
  
- No return value



!!! abstract "Version"
	This function requires Godot 4.3 or higher.


This function is useful if a script extension is not automatically applied. This situation can occur when a script is attached to a preloaded scene. If you encounter issues where your script extension is not working as expected, try to identify the scene to which it is attached and use this method to refresh it. This will reload already loaded scenes and apply the script extension.   

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 extend_scene(` `#!gd2 scene_vanilla_path:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 edit_callable:`&nbsp;&nbsp;[`#!gd2 Callable`](https://docs.godotengine.org/en/stable/classes/class_callable.html)`#!gd2 ) static ` {#method-extend_scene data-toc-label='extend_scene' .no-code-padding}
#### Description:
Extends a specific scene by providing a callable function to modify it.   
#### Parameters:
  
- `#!gd2 scene_vanilla_path` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the vanilla scene file.  
- `#!gd2 edit_callable` ([`#!gd2 Callable`](https://docs.godotengine.org/en/stable/classes/class_callable.html)): The callable function to modify the scene.

**Returns:**
  
- No return value

The callable receives an instance of the "vanilla_scene" as the first parameter.  

***
### • [`#!gd2 ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html)&nbsp;&nbsp;`#!gd2 get_mod_data(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_mod_data data-toc-label='get_mod_data' .no-code-padding}
#### Description:
Gets the [`#!gd2 ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) from the provided namespace.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd2 ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html): The [`#!gd2 ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) associated with the provided `#!gd2 mod_id`, or null if the `#!gd2 mod_id` is invalid.  

***
### • [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)&nbsp;&nbsp;`#!gd2 get_mod_data_all(` `#!gd2 ) static ` {#method-get_mod_data_all data-toc-label='get_mod_data_all' .no-code-padding}
#### Description:
Gets the [`#!gd2 ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) of all loaded Mods as [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html).

**Returns:**
  
- [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html): A dictionary containing the [`#!gd2 ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) of all loaded mods.  

***
### • [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)&nbsp;&nbsp;`#!gd2 get_unpacked_dir(` `#!gd2 ) static ` {#method-get_unpacked_dir data-toc-label='get_unpacked_dir' .no-code-padding}
#### Description:
Returns the path to the directory where unpacked mods are stored.

**Returns:**
  
- [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html): The path to the unpacked mods directory.  

***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 is_mod_loaded(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-is_mod_loaded data-toc-label='is_mod_loaded' .no-code-padding}
#### Description:
Returns true if the mod with the given `#!gd2 mod_id` was successfully loaded.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): true if the mod is loaded, false otherwise.  

***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 is_mod_active(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-is_mod_active data-toc-label='is_mod_active' .no-code-padding}
#### Description:
Returns true if the mod with the given mod_id was successfully loaded and is currently active.   
Parameters: - `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.   
Returns: - [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): true if the mod is loaded and active, false otherwise.
***
