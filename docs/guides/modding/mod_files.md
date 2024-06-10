# Mod Files
Mods you create must have the following 2 files:
- **mod_main.gd** - The init file for your mod
- **manifest.json** - Meta data for your mod

## mod_main.gd
*See [ModLoaderApi](api/ModLoaderApi.md) for more info*

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

!> The const variable you use to log (`AUTHORNAME_MODNAME_LOG_NAME` in the example above) should **always** be unique to your own mod, in every file you use it. Otherwise, if another mod uses that same variable, you'll get an error.


## manifest.json
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

?> This uses the structure of [Thunderstore packages](https://thunderstore.io/package/create/docs/), which means you can use the same manifest.json for both your mod and your Thunderstore package.


## Tips & Best Practices
GDScript has a style guide you can read [here](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html). Following the guide will help your code be more consistent, and make it easier to maintain and expand by other modders.

When naming files, use snake_case, and only use the characters `A-z`, `0-9`, and `_`.

?> ModLoader mods use hyphens (`-`) for mod names, but they shouldn't be used in any other case.

---

<div align="center">
  <b>Next:</b> <a href="#/api/mod_loader_api.md">API Methods</a>
</div>
