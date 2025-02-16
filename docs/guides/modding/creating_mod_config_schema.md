# Mod Configs
## Creating a Mod Config Schema with JSON-Schemas
### Setting Up Your Manifest File
To define your mod's configuration schema, you need to provide a JSON-Schema within your mod's manifest. Follow these steps to set it up:
1. Open your mod's `manifest.json` file.
2. Under the `"extra"` -> `"godot"` section, add a `"config_schema"` key as shown below:
```json
{
    "name": "ModName",
    "namespace": "GodotModding",
    "version_number": "0.2.0",
    "description": "Example Mod",
    "website_url": "https://github.com/GodotModding",
    "dependencies": [],
    "extra": {
        "godot": {
            "authors": ["GodotModding"],
            "optional_dependencies": [],
            "compatible_game_version": [],
            "compatible_mod_loader_version": ["6.2.0"],
            "incompatibilities": [],
            "load_before": [],
            "tags": [],
            "config_schema": {}
        }
    }
}
```


### Understanding JSON-Schema
Before diving into creating your mod's configuration schema, it's essential to understand JSON-Schemas. JSON-Schema is a powerful tool for validating and describing the structure of JSON data. To get started, we recommend reading the [Understanding JSON Schema](https://json-schema.org/understanding-json-schema) documentation. Use the introductory content and type pages as references when crafting your schema.

ModLoader supports most of the keys described in the [JSON Schema 2020-12 Draft](https://json-schema.org/draft/2020-12/release-notes.html). To view a complete list of unsupported and additional keys, check out the [Config JSON](config_json.md) section of our docs.


### Writing Your Config Schema
Now that you have a grasp of JSON-Schemas, it's time to create your Mod Config Schema. Let's break down the process:

#### The Schema "Head"
In the schema "head," you'll provide general information about your schema, such as its title and description. Although ModLoader doesn't use this information, it's considered best practice to include it. Here's a basic example:
```json
"config_schema": {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Config",
    "description": "Config for this Mod",
    "type": "object",
    "properties": {}
}
```

Feel free to customize the "title" and "description" to match your mod's specific configuration.


#### Defining Properties
The `"properties"` section is where you define what's allowed in your mod's configuration. Below are examples for different types of values:


##### Number Values and general structure
```json
"player_speed": {
    "type": "number",
    "title": "Player Speed Multiplier",
    "minimum": 0.1,
    "maximum": 2.0,
    "multipleOf": 0.1,
    "default": 1.0
}
```
- `"player_speed"`is the property key, used to access this specific config data later.
- `"type"` specifies the data type.
- `"title"` is the display title for this property, used by config UIs.
- `"minimum"` and "maximum" set the allowed number range.
- `"multipleOf"` defines the allowable increments for the number.
- `"default"` provides a default or starting value.


##### Boolean Values
```gdscript
"aim_assist": {
    "type": "boolean",
    "title": "Aim Assist",
    "default": false
}
```
For boolean values, simply include the `"default"` property.


##### String Values
```json
"character_name": {
	"title": "Character Name",
	"type": "string",
	"minLength": 3,
	"maxLength": 10,
	"default": "Udo"
}
```
For string values, you can use additional properties like `"minLength"` and `"maxLength"`. Check the [json-schema-docs](https://json-schema.org/understanding-json-schema/reference/string) for more details.


##### String Color Values
```json
"color": {
	"type": "string",
	"title": "Color",
	"format": "color",
	"default": "#f7000000"
}
```
The `"format: "color"` is a special case not covered in the [JSON Schema Draft](https://json-schema.org/draft/2020-12/release-notes.html). We've added it to Mod Loader for common color use cases. You can specify a default value in the ARGB format.

For additional keys and properties, refer to the [Config JSON](config_json.md) section of our docs.


## Conclusion
ModLoader will recognize the schema and automatically generate a default config based on it. Depending on the game, you should see the default config in the UI.

For more information about Mod Configs visit the following sides:
* [Config JSON](config_json.md)
* [ModLoaderConfig](../../api/mod_loader_config.md)

For further assistance, you can join us on [Discord](ttps://discord.gg/J5AvdFK4mw) or open a new [issue](https://github.com/GodotModding/godot-mod-loader/issues).
