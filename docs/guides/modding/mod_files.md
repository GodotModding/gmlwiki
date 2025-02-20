---
description: Overview of all required mod files.
---

# Mod Files

Every mod you create must have the following 2 files:

- [**manifest.json**](#manifestjson), which contains metadata for your mod, and
- [**mod_main.gd**](#mod_maingd), which is the entrypoint for your mod to start everything it needs

## manifest.json

The `manifest.json` is a special metadata file that tells the ModLoader information about your mod. You can edit
this file manually in Godot or in another editor of your choice, or by using the [Mod Tool](tools/mod_tool.md#manifest-editor), 
which provides validation and some editing help for each field.

It includes a few relatively self-explanatory fields like the mod's `name` and `description`, 
as well as the `namespace`, which is usually the authors name, or the name of the group of people that maintain the mod.
Both together create your final mod ID when attached together:  
`{namespace}-{name}`, for example `GodotModding-ExampleMod`.  
This is the identifier that the mod loader and other mods will use to manage your mod.
It also includes multiple ways of setting dependencies, which you can learn more about in the 
[using other mods](using_other_mods.md) guide.

```json
{
	"name": "ModName",
	"namespace": "AuthorName",
	"version_number": "1.0.0",
	"description": "Mod description goes here",
	"website_url": "https://github.com/example/repo",
	"dependencies": [
		"Add IDs of other mods here, if your mod needs them to work"
	],
	"extra": {
		"godot": {
			"authors": ["AuthorName"],
			"tags": ["tag1", "tag2"],
			"description_rich": "",
			"optional_dependencies": ["IDs your mod should load after if they are loaded"],
			"load_before": ["IDs your mod should load before"],
			"incompatibilities": [
				"Add IDs of other mods here, if your mod conflicts with them"
			],
			"compatible_mod_loader_version": ["6.2.0"],
			"compatible_game_version": ["1.2.3"],
			"config_schema": {}
		}
	}
}
```

???+ tip 
    The manifest uses the structure of [Thunderstore packages](https://thunderstore.io/package/create/docs/), 
    which means you can use the same `manifest.json` for both your mod and your Thunderstore package.

## mod_main.gd

See [ModLoaderApi](../../api/mod_loader_api.md) for more info on script extensions, translations and more.

```gdscript
extends Node


const AUTHORNAME_MODNAME_DIR := "AuthorName-ModName"
const AUTHORNAME_MODNAME_LOG_NAME := "AuthorName-ModName:Main"

var mod_dir_path := ""
var extensions_dir_path := ""
var translations_dir_path := ""

# Before v6.1.0
# func _init(modLoader = ModLoader) -> void:
func _init() -> void:
	mod_dir_path = ModLoaderMod.get_unpacked_dir().plus_file(AUTHORNAME_MODNAME_DIR)
	# Add extensions
	install_script_extensions()
	# Add translations
	add_translations()


func install_script_extensions() -> void:
	extensions_dir_path = mod_dir_path.plus_file("extensions")
	# extensions_dir_path = mod_dir_path.path_join("extensions") # Godot 4

        # ModLoaderMod.install_script_extension(extensions_dir_path.plus_file(...))



func add_translations() -> void:
	translations_dir_path = mod_dir_path.plus_file("translations")
        # ModLoaderMod.add_translation(translations_dir_path.plus_file(...))


func _ready() -> void:
	ModLoaderLog.info("Ready!", AUTHORNAME_MODNAME_LOG_NAME)
```

???+ note 
    The const variable you use to log (`AUTHORNAME_MODNAME_LOG_NAME` in the example above) should **always** be unique 
    to your own mod, in every file you use it. Otherwise, if another mod uses that same variable, you'll get an error.


## Tips & Best Practices
GDScript has a style guide you can read [here](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html). Following the guide will help your code be more consistent, and make it easier to maintain and expand by other modders.

When naming files, use snake_case, and only use the characters `A-z`, `0-9`, and `_`.

???+ note 
    ModLoader mods use hyphens (`-`) for mod names due to Thunderstore conventions, 
    but they shouldn't be used for any other file names.
