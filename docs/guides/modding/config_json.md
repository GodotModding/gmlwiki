---
description: The Godot ModLoader supports config files in the JSON format.
---

# Config JSON
The Godot ModLoader supports config files in the JSON format.


## JSON Schema
Mod developers can choose to add a [JSON Schema](https://json-schema.org/understanding-json-schema/) to their mod's manifest file using the `extra.godot.config_schema` key.

```json
{
    "extra": {
        "godot": {
            "config_schema": {
                "title": "Config",
                "description": "Config for this Mod",
                "type": "object",
                "properties": {
                    "example_text": {
                        "title": "Example text:",
                        "type": "string",
                        "default": "Some example string"
                    }
                }
            }
        }
    }
}
```


### Defaults
The `default` key in the schema is used to generate the default config.


### Unsupported Keys
The following keys are part of the [JSON Schema 2020-12 Draft](https://json-schema.org/draft/2020-12/release-notes.html) but are currently not supported by ModLoader:

| <p align=center>Type</p>   | <p align=center>Key</p> |
|----------------------------|-------------------------|
| Array                      | contains                |
| Array                      | minContains             |
| Array                      | maxContains             |
| Array                      | uniqueItems             |
| Object                     | patternProperties       |
| String                     | *format                 |

???+ note 
     The `format` key has one compatible property called `color` which is explained in more detail in the [Additional Keys and Properties](#additional-keys-and-properties) section. If you require any of these validations, please let us know by opening an [issue](https://github.com/GodotModding/godot-mod-loader/issues) or joining our [Discord](https://discord.gg/J5AvdFK4mw).


### Additional Keys and Properties
The following keys and properties are not part of the JSON Schema Draft but have been added for ease of use in ModLoader:

| Type   | Key    | Property | Description                               |
|--------|--------|----------|-------------------------------------------|
| String | format | color    | A hexadecimal color string in ARGB format |


### Color Example
```json
"color": {
	"type": "string",
	"title": "Color Over",
	"format": "color",
	"default": "#f7000000"
}
```


### Learn JSON Schema
For more details on how to write JSON Schemas, we recommend checking out [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/).


## Creating Configs
Mod users can choose to create their own configs by preferably using a [Config Editor UI]() provided by the game or a mod. If no UI is available, configs can be added by duplicating the default config file and modifying it. This is less ideal because the config is validated against the schema in the mod's manifest. Creating a valid config "by hand" requires checking the JSON Schema in the mod's manifest file.

Mod config files are stored in `user://configs/{mod_id}/{config_name}.json`. If a mod has a config, there should always be the `default.json` config file.


## Applying Configs to Your mod
You can retrieve the current config for your mod by calling `ModLoaderConfig.get_current_config("your_mod_id")`, which returns a `ModConfig` Resource.

A `ModConfig` resource contains:

| Property  | Description                                            |
|-----------|--------------------------------------------------------|
| name      | The config name                                        |
| mod_id    | The mod_id this config belongs to                      |
| schema    | The schema for your configs                            |
| data      | The data this config holds                             |
| save_path | The path where the JSON file for this config is stored |
| is_valid  | False if any data is invalid                           |

For mod developers, the `data` property is the most relevant. Depending on how the config selection is implemented, you might want to check if the config is valid using `is_valid`.

With all this in mind, you can add something like the following code to your `mod_main.gd` `ready()` function:

**mod_main.gd**
```gdscript2
_ready(): 
	# Get the current config
	var config = ModLoaderConfig.get_current_config("your_mod_id")

	# Connect to current_config_changed signal
	ModLoader.connect("current_config_changed", self, "_on_current_config_changed")

	# Apply configs
	apply_config(config)


func apply_config(config: ModConfig) -> void:
	# Code to apply the config
	# In this example, an 'apply_config' function is called in a different scene
	different_scene.call_deferred("apply_config", config)


func _on_current_config_changed(config: ModConfig) -> void:
	# Check if the config of your mod has changed!
	if config.mod_id == "your_mod_id":
		apply_config(config)
```

**different_scene.gd**
```gdscript2
func apply_config(config: ModConfig) -> void:
	label_select_profile.text = config.data.select_profile_text

	var material_settings: Dictionary = config.data.material_settings
	
	material.set_shader_param("animate", material_settings.animate)
	material.set_shader_param("square_scale", material_settings.square_scale)
	material.set_shader_param("blur_amount", material_settings.blur_amount)
	material.set_shader_param("mix_amount", material_settings.mix_amount)
	material.set_shader_param("color_over", Color(material_settings.color))
```
