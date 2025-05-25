---
description: Class for managing per-mod configurations.
---

# ModLoaderConfig
**Inherits**: Object


Class for managing per-mod configurations.
<hr style="border-width: thick">

## Constants
#### • `#!gd2 LOG_NAME`: `#!gd2 "ModLoader:Config"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 
#### • `#!gd2 DEFAULT_CONFIG_NAME`: `#!gd2 "default"` {#constant-DEFAULT_CONFIG_NAME data-toc-label='DEFAULT_CONFIG_NAME'} 

<hr style="border-width: thick">

## Method Descriptions
### • [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)&nbsp;&nbsp;`#!gd2 create_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 config_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 config_data:`&nbsp;&nbsp;[`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)`#!gd2 ) static ` {#method-create_config data-toc-label='create_config' .no-code-padding}
#### Description:
Creates a new configuration for a mod.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd2 config_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the configuration.  
- `#!gd2 config_data` ([`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)): The configuration data to be stored.

**Returns:**
  
- [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The created [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object if successful, or null otherwise.
***
### • [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)&nbsp;&nbsp;`#!gd2 update_config(` `#!gd2 config:`&nbsp;&nbsp;[`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)`#!gd2 ) static ` {#method-update_config data-toc-label='update_config' .no-code-padding}
#### Description:
Updates an existing [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object with new data and saves the config file.

#### Parameters:
  
- `#!gd2 config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object to be updated.

**Returns:**
  
- [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The updated [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object if successful, or null otherwise.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 delete_config(` `#!gd2 config:`&nbsp;&nbsp;[`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)`#!gd2 ) static ` {#method-delete_config data-toc-label='delete_config' .no-code-padding}
#### Description:
Deletes a [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object and performs cleanup operations.

#### Parameters:
  
- `#!gd2 config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object to be deleted.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the deletion was successful, False otherwise.
***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 set_current_config(` `#!gd2 config:`&nbsp;&nbsp;[`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)`#!gd2 ) static ` {#method-set_current_config data-toc-label='set_current_config' .no-code-padding}
#### Description:
Sets the current configuration of a mod to the specified configuration.

#### Parameters:
  
- `#!gd2 config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object to be set as current config.
***
### • [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)&nbsp;&nbsp;`#!gd2 get_config_schema(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_config_schema data-toc-label='get_config_schema' .no-code-padding}
#### Description:
Returns the schema for the specified mod id.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- A dictionary representing the schema for the mod's configuration file.
***
### • [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)&nbsp;&nbsp;`#!gd2 get_schema_for_prop(` `#!gd2 config:`&nbsp;&nbsp;[`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)`#!gd2 , ` `#!gd2 prop:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_schema_for_prop data-toc-label='get_schema_for_prop' .no-code-padding}
#### Description:
Retrieves the schema for a specific property key.

#### Parameters:
  
- `#!gd2 config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object from which to retrieve the schema.  
- `#!gd2 prop` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The property key for which to retrieve the schema.

**Returns:**
  
- [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html): The schema dictionary for the specified property.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_mods_with_config(` `#!gd2 ) static ` {#method-get_mods_with_config data-toc-label='get_mods_with_config' .no-code-padding}
#### Description:
Retrieves an Array of mods that have configuration files.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An Array containing the mod data of mods that have configuration files.
***
### • [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)&nbsp;&nbsp;`#!gd2 get_configs(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_configs data-toc-label='get_configs' .no-code-padding}
#### Description:
Retrieves the configurations dictionary for a given mod ID.

#### Parameters:
  
- `#!gd2 mod_id`: The ID of the mod.

**Returns:**
  
- [`#!gd2 Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html): A dictionary containing the configurations for the specified mod. If the mod ID is invalid or no configurations are found, an empty dictionary is returned.
***
### • [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)&nbsp;&nbsp;`#!gd2 get_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 config_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_config data-toc-label='get_config' .no-code-padding}
#### Description:
Retrieves the configuration for a specific mod and configuration name.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd2 config_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the configuration.

**Returns:**
  
- [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The configuration as a [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object or null if not found.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 has_current_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-has_current_config data-toc-label='has_current_config' .no-code-padding}
#### Description:
Checks whether a mod has a current configuration set.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the mod has a current configuration, false otherwise.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 has_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 config_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-has_config data-toc-label='has_config' .no-code-padding}
#### Description:
Checks whether a mod has a configuration with the specified name.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd2 config_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the configuration.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the mod has a configuration with the specified name, False otherwise.
***
### • [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)&nbsp;&nbsp;`#!gd2 get_default_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_default_config data-toc-label='get_default_config' .no-code-padding}
#### Description:
Retrieves the default configuration for a specified mod ID.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object representing the default configuration for the specified mod. If the mod ID is invalid or no configuration is found, returns null.
***
### • [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)&nbsp;&nbsp;`#!gd2 get_current_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_current_config data-toc-label='get_current_config' .no-code-padding}
#### Description:
Retrieves the currently active configuration for a specific mod.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The configuration as a [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object or `#!gd2 null` if not found.
***
### • [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)&nbsp;&nbsp;`#!gd2 get_current_config_name(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_current_config_name data-toc-label='get_current_config_name' .no-code-padding}
#### Description:
Retrieves the name of the current configuration for a specific mod.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html) The currently active configuration name for the given mod id or an empty string if not found.
***
### • [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)&nbsp;&nbsp;`#!gd2 refresh_config_data(` `#!gd2 config:`&nbsp;&nbsp;[`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)`#!gd2 ) static ` {#method-refresh_config_data data-toc-label='refresh_config_data' .no-code-padding}
#### Description:
Refreshes the data of the provided configuration by reloading it from the config file.

#### Parameters:
  
- `#!gd2 config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object whose data needs to be refreshed.

**Returns:**
  
- [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The [`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object with refreshed data if successful, or the original object otherwise.
***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 refresh_current_configs(` `#!gd2 ) static ` {#method-refresh_current_configs data-toc-label='refresh_current_configs' .no-code-padding}
#### Description:
Iterates over all mods to refresh the data of their current configurations, if available.

**Returns:**
  
- No return value

Compares the previous configuration data with the refreshed data and emits the [signal ModLoader.current_config_changed] signal if changes are detected.  
This function ensures that any changes made to the configuration files outside the application are reflected within the application's runtime, allowing for dynamic updates without the need for a restart.
***
