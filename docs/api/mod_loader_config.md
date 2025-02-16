# ModLoaderConfig
**Inherits**: Object


Class for managing per-mod configurations.
<hr style="border-width: thick">

## Constants
#### • `#!gd LOG_NAME`: `#!gd "ModLoader:Config"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 
#### • `#!gd DEFAULT_CONFIG_NAME`: `#!gd "default"` {#constant-DEFAULT_CONFIG_NAME data-toc-label='DEFAULT_CONFIG_NAME'} 

<hr style="border-width: thick">

## Method Descriptions
### • [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) <code class="highlight">create_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), config_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), config_data: [Dictionary](https://docs.godotengine.org/en/stable/classes/class_dictionary.html))</code> static {#method-create_config data-toc-label='create_config'}
#### Description:
Creates a new configuration for a mod.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd config_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the configuration.  
- `#!gd config_data` ([`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html)): The configuration data to be stored.

**Returns:**
  
- [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The created [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object if successful, or null otherwise.
***
### • [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) <code class="highlight">update_config(config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html))</code> static {#method-update_config data-toc-label='update_config'}
#### Description:
Updates an existing [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object with new data and saves the config file.

#### Parameters:
  
- `#!gd config` ([`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object to be updated.

**Returns:**
  
- [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The updated [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object if successful, or null otherwise.
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">delete_config(config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html))</code> static {#method-delete_config data-toc-label='delete_config'}
#### Description:
Deletes a [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object and performs cleanup operations.

#### Parameters:
  
- `#!gd config` ([`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object to be deleted.

**Returns:**
  
- [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the deletion was successful, False otherwise.
***
### • void <code class="highlight">set_current_config(config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html))</code> static {#method-set_current_config data-toc-label='set_current_config'}
#### Description:
Sets the current configuration of a mod to the specified configuration.

#### Parameters:
  
- `#!gd config` ([`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object to be set as current config.
***
### • [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html) <code class="highlight">get_config_schema(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_config_schema data-toc-label='get_config_schema'}
#### Description:
Returns the schema for the specified mod id.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- A dictionary representing the schema for the mod's configuration file.
***
### • [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html) <code class="highlight">get_schema_for_prop(config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html), prop: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_schema_for_prop data-toc-label='get_schema_for_prop'}
#### Description:
Retrieves the schema for a specific property key.

#### Parameters:
  
- `#!gd config` ([`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object from which to retrieve the schema.  
- `#!gd prop` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The property key for which to retrieve the schema.

**Returns:**
  
- [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html): The schema dictionary for the specified property.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_mods_with_config()</code> static {#method-get_mods_with_config data-toc-label='get_mods_with_config'}
#### Description:
Retrieves an Array of mods that have configuration files.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An Array containing the mod data of mods that have configuration files.
***
### • [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html) <code class="highlight">get_configs(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_configs data-toc-label='get_configs'}
#### Description:
Retrieves the configurations dictionary for a given mod ID.

#### Parameters:
  
- `#!gd mod_id`: The ID of the mod.

**Returns:**
  
- [`#!gd Dictionary`](https://docs.godotengine.org/en/stable/classes/class_dictionary.html): A dictionary containing the configurations for the specified mod. If the mod ID is invalid or no configurations are found, an empty dictionary is returned.
***
### • [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) <code class="highlight">get_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), config_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_config data-toc-label='get_config'}
#### Description:
Retrieves the configuration for a specific mod and configuration name.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd config_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the configuration.

**Returns:**
  
- [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The configuration as a [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object or null if not found.
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">has_current_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-has_current_config data-toc-label='has_current_config'}
#### Description:
Checks whether a mod has a current configuration set.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the mod has a current configuration, false otherwise.
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">has_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), config_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-has_config data-toc-label='has_config'}
#### Description:
Checks whether a mod has a configuration with the specified name.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd config_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the configuration.

**Returns:**
  
- [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the mod has a configuration with the specified name, False otherwise.
***
### • [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) <code class="highlight">get_default_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_default_config data-toc-label='get_default_config'}
#### Description:
Retrieves the default configuration for a specified mod ID.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object representing the default configuration for the specified mod. If the mod ID is invalid or no configuration is found, returns null.
***
### • [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) <code class="highlight">get_current_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_current_config data-toc-label='get_current_config'}
#### Description:
Retrieves the currently active configuration for a specific mod.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The configuration as a [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object or `#!gd null` if not found.
***
### • [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_current_config_name(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_current_config_name data-toc-label='get_current_config_name'}
#### Description:
Retrieves the name of the current configuration for a specific mod.

#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.

**Returns:**
  
- [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html) The currently active configuration name for the given mod id or an empty string if not found.
***
### • [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) <code class="highlight">refresh_config_data(config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html))</code> static {#method-refresh_config_data data-toc-label='refresh_config_data'}
#### Description:
Refreshes the data of the provided configuration by reloading it from the config file.

#### Parameters:
  
- `#!gd config` ([`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object whose data needs to be refreshed.

**Returns:**
  
- [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html): The [`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html) object with refreshed data if successful, or the original object otherwise.
***
### • void <code class="highlight">refresh_current_configs()</code> static {#method-refresh_current_configs data-toc-label='refresh_current_configs'}
#### Description:
Iterates over all mods to refresh the data of their current configurations, if available.

**Returns:**
  
- No return value

Compares the previous configuration data with the refreshed data and emits the [signal ModLoader.current_config_changed] signal if changes are detected.  
This function ensures that any changes made to the configuration files outside the application are reflected within the application's runtime, allowing for dynamic updates without the need for a restart.
***
