
Provides methods to manage mod state.

!!! example "Experimental"
    This class may be unstable


## Methods Overview
| Method                                                      | Description                   |
|-------------------------------------------------------------|-------------------------------|
| [`uninstall_script_extension`](#uninstall_script_extension) | Uninstall a script extension. |
| [`reload_mods`](#reload_mods)                               | Reload all mods.              |
| [`disable_mods`](#disable_mods)                             | Disable all mods.             |
| [`disable_mod`](#disable_mod)                               | Disable a mod.                |

## Methods
### uninstall_script_extension
```gdscript
func uninstall_script_extension(extension_script_path: String) -> void:
```
Uninstall a script extension.

Parameters:
- extension_script_path (String): The path to the extension script to be uninstalled.


### reload_mods
```gdscript
func reload_mods() -> void
```
Reload all mods.

?> This function should be called only when actually necessary as it can break the game and require a restart for mods that do not fully use the systems put in place by the mod loader, so anything that just uses add_node, move_node ecc... To not have your mod break on reload please use provided functions like ModLoader::save_scene, ModLoader::append_node_in_scene and all the functions that will be added in the next versions Used to reload already present mods and load new ones


### disable_mods
```gdscript
func disable_mods() -> void
```
Disable all mods.

?> This function should be called only when actually necessary as it can break the game and require a restart for mods that do not fully use the systems put in place by the mod loader, so anything that just uses add_node, move_node ecc... To not have your mod break on disable please use provided functions and implement a _disable function in your mod_main.gd that will handle removing all the changes that were not done through the Mod Loader


### disable_mod
Disable a mod.

?> Note: This function should be called only when actually necessary as it can break the game and require a restart for mods that do not fully use the systems put in place by the mod loader, so anything that just uses add_node, move_node ecc... To not have your mod break on disable please use provided functions and implement a _disable function in your mod_main.gd that will handle removing all the changes that were not done through the Mod Loader

Parameters:
- mod_data (ModData): The ModData object representing the mod to be disabled.