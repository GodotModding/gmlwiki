<!-- top of file anchor -->
<a name="top"></a>

# ModLoaderConfig
This class provides functionality for working with per-mod Configurations.

## Methods Overview
<!-- should this be turned into an HTML table to avoid creating huge md tables? -->
| Method                                               | Description                                                                                                                                                               |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`create_config`](#create_config)                    | Creates a new configuration for a mod.                                                                                                                                    |
| [`update_config`](#update_config)                    | Updates an existing ModConfig object with new data and save the config file.                                                                                              |
| [`delete_config`](#delete_config)                    | Deletes a ModConfig object and performs cleanup operations.                                                                                                               |
| [`set_current_config`](#set_current_config)          | Sets the current configuration of a mod to the specified configuration.                                                                                                   |
| [`get_config_schema`](#get_config_schema)            | Returns the schema for the specified mod id. If no configuration file exists for the mod, an empty dictionary is returned.                                                |
| [`get_schema_for_prop`](#get_schema_for_prop)        | Retrieves the schema for a specific property key.                                                                                                                         |
| [`get_mods_with_config`](#get_mods_with_config)      | Retrieves an Array of mods that have configuration files.                                                                                                                 |
| [`get_configs`](#get_configs)                        | Retrieves the configurations dictionary for a given mod ID.                                                                                                               |
| [`get_config`](#get_config)                          | Retrieves the configuration for a specific mod and configuration name. Returns the configuration as a ModConfig object or null if not found.                              |
| [`get_default_config`](#get_default_config)           | Retrieves the default configuration for a specified mod ID.                                                                                                               |
| [`get_current_config`](#get_current_config)           | Retrieves the currently active configuration for a specific mod                                                                                                           |
| [`get_current_config_name`](#get_current_config_name) | Retrieves the name of the current configuration for a specific mod Returns an empty string if no configuration exists for the mod or the user profile has not been loaded |

## Methods
### create_config
```gdscript
func create_config(mod_id: String, config_name: String, config_data: Dictionary) -> ModConfig
```
Creates a new configuration for a mod.

Parameters:
- mod_id (String): The ID of the mod for which the configuration is being created.
- config_name (String): The name of the configuration.
- config_data (Dictionary): The configuration data to be stored in the new configuration.

Returns:
- ModConfig: The created ModConfig object if successful, or null otherwise.


### update_config
```gdscript
func update_config(config: ModConfig) -> ModConfig
```
Updates an existing ModConfig object with new data and save the config file.

Parameters:
- config (ModConfig): The ModConfig object to be updated.

Returns:
- ModConfig: The updated ModConfig object if successful, or null otherwise.


### delete_config
```gdscript
func delete_config(config: ModConfig) -> bool
```
Deletes a ModConfig object and performs cleanup operations.

Parameters:
- config (ModConfig): The ModConfig object to be deleted.

Returns:
- bool: True if the deletion was successful, False otherwise.


### set_current_config
```gdscript
func set_current_config(config: ModConfig) -> void
```
Sets the current configuration of a mod to the specified configuration.

Parameters:
- config (ModConfig): The ModConfig object to be set as current config.


### get_config_schema
```gdscript
func get_config_schema(mod_id: String) -> Dictionary
```
Returns the schema for the specified mod id. If no configuration file exists for the mod, an empty dictionary is returned.

Parameters:
- mod_id (String): the ID of the mod to get the configuration schema for

Returns:
- A dictionary representing the schema for the mod's configuration file


### get_schema_for_prop
```gdscript
func get_schema_for_prop(config: ModConfig, prop: String) -> Dictionary
```
Retrieves the schema for a specific property key.

Parameters:
- config (ModConfig): The ModConfig object from which to retrieve the schema.
- prop (String): The property key for which to retrieve the schema. e.g. `parentProp.childProp.nthChildProp` or `propKey`

Returns:
- Dictionary: The schema dictionary for the specified property.


### get_mods_with_config
```gdscript
func get_mods_with_config() -> Array
```
Retrieves an Array of mods that have configuration files.

Returns:
- An Array containing the mod data of mods that have configuration files.


### get_configs
```gdscript
func get_configs(mod_id: String) -> Dictionary
```
Retrieves the configurations dictionary for a given mod ID.

Parameters:
- mod_id: The ID of the mod for which to retrieve the configurations.

Returns:
- A dictionary containing the configurations for the specified mod. If the mod ID is invalid or no configurations are found, an empty dictionary is returned.


### get_config
```gdscript
func get_config(mod_id: String, config_name: String) -> ModConfig
```
Retrieves the configuration for a specific mod and configuration name. Returns the configuration as a ModConfig object or null if not found.

Parameters:
- mod_id (String): The ID of the mod to retrieve the configuration for.
- config_name (String): The name of the configuration to retrieve.

Returns:
- The configuration as a ModConfig object or null if not found.


### get_default_config
```gdscript
func get_default_config(mod_id: String) -> ModConfig
```
Retrieves the default configuration for a specified mod ID.

Parameters:
- mod_id: The ID of the mod for which to retrieve the default configuration.

Returns:
- The ModConfig object representing the default configuration for the specified mod. If the mod ID is invalid or no configuration is found, returns null.


### get_current_config
```gdscript
func get_current_config(mod_id: String) -> ModConfig
```
Retrieves the currently active configuration for a specific mod

Parameters:
- mod_id (String): The ID of the mod to retrieve the configuration for.

Returns:
- The configuration as a ModConfig object or null if not found.


### get_current_config_name
```gdscript
func get_current_config_name(mod_id: String) -> String
```
Retrieves the name of the current configuration for a specific mod Returns an empty string if no configuration exists for the mod or the user profile has not been loaded

Parameters:
- mod_id (String): The ID of the mod to retrieve the current configuration name for.

Returns:
- The currently active configuration name for the given mod id or an empty string if not found.


## Constants Descriptions
##### DEFAULT_CONFIG_NAME
```gdscript
const DEFAULT_CONFIG_NAME: String = "default"
```


##### LOG_NAME
```gdscript
const LOG_NAME: String = "ModLoader:Config"
```