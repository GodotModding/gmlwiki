---
status: new
description: This Class provides helper functions to build mods.
---

# ModLoaderMod
**Inherits**: Object


This Class provides helper functions to build mods.
<hr style="border-width: thick">

## Constants
#### • `#!gd LOG_NAME`: `#!gd "ModLoader:Mod"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 

<hr style="border-width: thick">

## Method Descriptions
### • void <code class="highlight">install_script_extension(child_script_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-install_script_extension data-toc-label='install_script_extension'}
#### Description:
Installs a script extension that extends a vanilla script.

#### Parameters:
  
- `#!gd child_script_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the mod's extender script.

**Returns:**
  
- No return value

This is the preferred way of modifying a vanilla [`#!gd Script`](https://docs.godotengine.org/en/stable/classes/class_script.html)  
Since Godot 4, extensions can cause issues with scripts that use `#!gd class_name` and should be avoided if present.  
See [`#!gd add_hook()`](#method-add_hook) for those cases.

The `#!gd child_script_path` should point to your mod's extender script.  
Example: `#!gd "MOD/extensions/singletons/utils.gd"`  
Inside the extender script, include `#!gd extends {target}` where `#!gd {target}` is the vanilla path.  
Example: `#!gd extends "res://singletons/utils.gd"`.  


!!! note 
	Your extender script doesn't have to follow the same directory path as the vanilla file, but it's good practice to do so.



***
### • void <code class="highlight">install_script_hooks(vanilla_script_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), hook_script_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-install_script_hooks data-toc-label='install_script_hooks'}
#### Description:
Adds all methods from a file as hooks. 

#### Parameters:
  
- `#!gd vanilla_script_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the script which will be hooked.  
- `#!gd hook_script_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the script containing hooks.

**Returns:**
  
- No return value

The file needs to extend [`#!gd Object`](https://docs.godotengine.org/en/stable/classes/class_object.html).  
The methods in the file need to have the exact same name as the vanilla method they intend to hook, all mismatches will be ignored.   
See: [`#!gd add_hook()`](#method-add_hook)   
#### Examples:
  

```gdscript 
ModLoaderMod.install_script_hooks(
    "res://tools/utilities.gd",
    extensions_dir_path.path_join("tools/utilities-hook.gd")
)
```
***
### • void <code class="highlight">add_hook(mod_callable: [Callable](https://docs.godotengine.org/en/stable/classes/class_callable.html), script_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), method_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-add_hook data-toc-label='add_hook'}
#### Description:
Adds a hook, a custom mod function, to a vanilla method.

#### Parameters:
  
- `#!gd mod_callable` ([`#!gd Callable`](https://docs.godotengine.org/en/stable/classes/class_callable.html)): The function that will executed when the vanilla method is executed. When writing a mod callable, make sure that it *always* receives a [`#!gd ModLoaderHookChain`](mod_loader_hook_chain.md) object as first argument, which is used to continue down the hook chain (see: [`#!gd ModLoaderHookChain.execute_next()`](mod_loader_hook_chain.md#method-execute_next)) and allows manipulating parameters before and return values after the vanilla method is called.   
- `#!gd script_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): Path to the vanilla script that holds the method.  
- `#!gd method_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The method the hook will be applied to.

**Returns:**


- No return value

Opposed to script extensions, hooks can be applied to scripts that use `#!gd class_name` without issues.  
If possible, prefer [`#!gd install_script_extension()`](#method-install_script_extension).

#### Examples:


Given the following vanilla script `#!gd main.gd`
```gdscript 
class_name MainGame
extends Node2D

var version := "vanilla 1.0.0"


func _ready():
    $CanvasLayer/Control/Label.text = "Version: %s" % version
    print(Utilities.format_date(15, 11, 2024))
```
 It can be hooked in `#!gd mod_main.gd` like this
```gdscript 
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
### • void <code class="highlight">register_global_classes_from_array(new_global_classes: [Array](https://docs.godotengine.org/en/stable/classes/class_array.html))</code> static {#method-register_global_classes_from_array data-toc-label='register_global_classes_from_array'}
#### Description:
Registers an array of classes to the global scope since Godot only does that in the editor.

#### Parameters:
  
- `#!gd new_global_classes` ([`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of class definitions to be registered.

**Returns:**
  
- No return value

Format: `#!gd { "base": "ParentClass", "class": "ClassName", "language": "GDScript", "path": "res://path/class_name.gd" }`



!!! tip 
	You can find these easily in the project.godot file under `_global_script_classes`
	(but you should only include classes belonging to your mod)
  

***
### • void <code class="highlight">add_translation(resource_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-add_translation data-toc-label='add_translation'}
#### Description:
Adds a translation file.

#### Parameters:
  
- `#!gd resource_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the translation resource file.  
**Returns:**
  
- No return value



!!! note 
	The `#!gd .translation` file should have been created by the Godot editor already, usually when importing a CSV file. The translation file should named `#!gd name.langcode.translation` -> `#!gd mytranslation.en.translation`.
  

***
### • void <code class="highlight">refresh_scene(scene_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-refresh_scene data-toc-label='refresh_scene'}
#### Description:
Marks the given scene for to be refreshed. It will be refreshed at the correct point in time later.

#### Parameters:
  
- `#!gd scene_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the scene file to be refreshed.   
**Returns:**
  
- No return value



!!! abstract "Version"
	This function requires Godot 4.3 or higher.


This function is useful if a script extension is not automatically applied. This situation can occur when a script is attached to a preloaded scene. If you encounter issues where your script extension is not working as expected, try to identify the scene to which it is attached and use this method to refresh it. This will reload already loaded scenes and apply the script extension.   

***
### • void <code class="highlight">extend_scene(scene_vanilla_path: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), edit_callable: [Callable](https://docs.godotengine.org/en/stable/classes/class_callable.html))</code> static {#method-extend_scene data-toc-label='extend_scene'}
#### Description:
Extends a specific scene by providing a callable function to modify it.   
#### Parameters:
  
- `#!gd scene_vanilla_path` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The path to the vanilla scene file.  
- `#!gd edit_callable` ([`#!gd Callable`](https://docs.godotengine.org/en/stable/classes/class_callable.html)): The callable function to modify the scene.

**Returns:**
  
- No return value

The callable receives an instance of the "vanilla_scene" as the first parameter.  

***
### • [`#!gd ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) <code class="highlight">get_mod_data(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_mod_data data-toc-label='get_mod_data'}
#### Description:
Gets the [`#!gd ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) from the provided namespace.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html): The [`#!gd ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) associated with the provided `#!gd mod_id`, or null if the `#!gd mod_id` is invalid.  

***
### • [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html) <code class="highlight">get_mod_data_all()</code> static {#method-get_mod_data_all data-toc-label='get_mod_data_all'}
#### Description:
Gets the [`#!gd ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) of all loaded Mods as [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html).

**Returns:**
  
- [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html): A dictionary containing the [`#!gd ModData`](https://docs.godotengine.org/en/stable/classes/class_moddata.html) of all loaded mods.  

***
### • [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_unpacked_dir()</code> static {#method-get_unpacked_dir data-toc-label='get_unpacked_dir'}
#### Description:
Returns the path to the directory where unpacked mods are stored.

**Returns:**
  
- [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html): The path to the unpacked mods directory.  

***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">is_mod_loaded(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-is_mod_loaded data-toc-label='is_mod_loaded'}
#### Description:
Returns true if the mod with the given `#!gd mod_id` was successfully loaded.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): true if the mod is loaded, false otherwise.  

***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">is_mod_active(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-is_mod_active data-toc-label='is_mod_active'}
#### Description:
Returns true if the mod with the given mod_id was successfully loaded and is currently active.   
Parameters: - `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.   
Returns: - [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): true if the mod is loaded and active, false otherwise.
***
