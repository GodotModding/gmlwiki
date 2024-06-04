# ModLoaderMod
This class provides helper functions to build mods. **These are the main methods your mods will use.**


## Methods Overview
| Method                                                                      | Description                                                                                 |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [`install_script_extension`](#install_script_extension)                     | Install a script extension that extends a vanilla script.                                   |
| [`register_global_classes_from_array`](#register_global_classes_from_array) | Register an array of classes to the global scope, since Godot only does that in the editor. |
| [`add_translation`](#add_translation)                                       | Add a translation file.                                                                     |
| [`get_mod_data`](#get_mod_data)                                             | Gets the ModData from the provided namespace.                                               |
| [`get_mod_data_all`](#get_mod_data_all)                                     | Gets the ModData of all loaded Mods as Dictionary.                                          |
| [`is_mod_loaded`](#is_mod_loaded)                                           | Returns true if the mod with the given mod_id was successfully loaded.                      |
| [`append_node_in_scene`](#append_node_in_scene)                             | Appends a new node to a modified scene.                                                     |
| [`save_scene`](#save_scene)                                                 | Saves a modified scene to a file.                                                           |
| [`get_unpacked_dir`](#get_unpacked_dir)                                     | Returns the path to the directory where unpacked mods are stored.                           |


## Methods
### install_script_extension
```gdscript
func install_script_extension(child_script_path: String) -> void
```
Install a script extension that extends a vanilla script. The child_script_path should point to your mod's extender script.

Example: `"MOD/extensions/singletons/utils.gd"`

Inside the extender script, include `extends {target}` where `{target}` is the vanilla path.

Example: `extends "res://singletons/utils.gd"`.

?> Your extender script doesn't have to follow the same directory path as the vanilla file, but it's good practice to do so.

*To learn more about script extensions, read: [Script-Extensions](/reference/script_extensions)*

Parameters:
- child_script_path (String): The path to the mod's extender script.


### register_global_classes_from_array
```gdscript
func register_global_classes_from_array(new_global_classes: Array) -> void
```
Register an array of classes to the global scope since Godot only does that in the editor.

Format: `{ "base": "ParentClass", "class": "ClassName", "language": "GDScript", "path": "res://path/class_name.gd" }`

You can find these easily in the project.godot file under _global_script_classes (but you should only include classes belonging to your mod)

?> Using this method creates the override.cfg file in the game directory. If a mod uses it, the player is required to restart the game once, otherwise it may cause a crash as elements referred to by the class will be inaccessible. Additionally, any other Godot application (like the workshop uploader) will crash due to mismatched project settings.

Parameters:
- new_global_classes (Array): An array of class definitions to be registered.


### add_translation
```gdscript
func add_translation(resource_path: String) -> void
```
Add a translation file.

?> The translation file should have been created in Godot already, such as when importing a CSV file. The translation file should be in the format mytranslation.en.translation.

Parameters:
- resource_path (String): The path to the translation resource file.


### get_mod_data
```gdscript
func get_mod_data(mod_id: String) -> ModData
```
Gets the ModData from the provided namespace

Parameters:
- mod_id (String): The ID of the mod.

Returns:
- ModData: The ModData associated with the provided mod_id, or null if the mod_id is invalid.


### get_mod_data_all
```gdscript
func get_mod_data_all() -> Dictionary
```
Gets the ModData of all loaded Mods as Dictionary.

Returns:
- Dictionary: A dictionary containing the ModData of all loaded mods.


### is_mod_loaded
```gdscript
func is_mod_loaded(mod_id: String) -> bool
```
Returns true if the mod with the given mod_id was successfully loaded.

Parameters:
- mod_id (String): The ID of the mod.

Returns:
- bool: true if the mod is loaded, false otherwise.


### append_node_in_scene
```gdscript
func append_node_in_scene(modified_scene: Node, node_name: String = "", node_parent = null, instance_path: String = "", is_visible: bool = true) -> void
```
Appends a new node to a modified scene.

Parameters:
- modified_scene (Node): The modified scene where the node will be appended.
- node_name (String): (Optional) The name of the new node. Default is an empty string.
- node_parent (Node): (Optional) The parent node where the new node will be added. Default is null (direct child of modified_scene).
- instance_path (String): (Optional) The path to a scene resource that will be instantiated as the new node. Default is an empty string resulting in a Node instance.
- is_visible (bool): (Optional) If true, the new node will be visible. Default is true.


### save_scene
```gdscript
func save_scene(modified_scene: Node, scene_path: String) -> void
```
Saves a modified scene to a file.

Parameters:
- modified_scene (Node): The modified scene instance to be saved.
- scene_path (String): The path to the scene file that will be replaced.


### get_unpacked_dir
```gdscript
func get_unpacked_dir() -> String
```
Returns the path to the directory where unpacked mods are stored.

Returns:
- String: The path to the unpacked mods directory.


## Constants Descriptions
##### LOG_NAME
```gdscript
const LOG_NAME: String = "ModLoader:Mod"
```