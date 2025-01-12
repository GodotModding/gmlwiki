# Breaking Changes
This page lists any breaking changes that occur with ModLoader releases.

## [v6.1.0](https://github.com/GodotModding/godot-mod-loader/releases/tag/v6.1.0)
Please note that this update may break mods that still rely on the `modLoader` argument in their `_init()` function. To mitigate this, a fallback and deprecation warning has been implemented that passes `self` as an argument if any arguments are detected in the `mod_main.gd` `_init()` function.

## [v6.0.2](https://github.com/GodotModding/godot-mod-loader/releases/tag/v6.0.2)
It is no longer allowed to have the same `mod_id` listed in both the `optional_dependencies` and `dependencies` sections, or in both the `load_before` and `incompatibilities` sections.

However, since the `optional_dependencies` and `load_before` features were introduced in [v6.0.0](https://github.com/GodotModding/godot-mod-loader/releases/tag/v6.0.0), it is highly unlikely that such conflicts exist.

## [v6.0.1](https://github.com/GodotModding/godot-mod-loader/releases/tag/v6.0.1)
Mods are now **always** unpacked and loaded into ModLoaderStore.mod_data. This change can potentially break mod lists that rely on having only loaded mods in `mod_data`. Consequently, these mod lists may display mods that are currently not loaded. To address this issue, authors of mod lists need to adapt their code to check the new `is_active` flag.

## [v6.0.0](https://github.com/GodotModding/godot-mod-loader/releases/tag/v6.0.0)
### Deprecation Messages
As outlined in the [v6 release notes](https://github.com/GodotModding/godot-mod-loader/releases/tag/v6.0.0), ModLoader v6 has refactored its entire codebase. This meant we needed to deprecate certain methods and classes, but we've also added new deprecation methods to ensure these changes won't break active mods.

If you try to use an old method, you'll get an error in the editor until it's fixed. The error message will tell you exactly what needs to change.

See the [Deprecated](#deprecated) section below for the full list of changes.

### Public Classes (API)
There are several new classes in the `api` directory, which is where all the publicly accessible methods are. These replace using `ModLoader.*` and `ModLoaderUtils.*` (see [Deprecated](#deprecated) below). The main classes you'll use are:
* [ModLoaderMod](../api/ModLoaderMod.md) - Everything related to mod setup, such as [`install_script_extension()`](../api/ModLoaderMod.md?id=install_script_extension).
* [ModLoaderLog](../api/ModLoaderLog.md) - All logging methods.

### Internal Classes
Some mods directly accessed variables and constants on `ModLoader`, for example `mod_data` or `UNPACKED_DIR`. Data such as this is now considered internal, and should not be accessed directly (this includes any method/variable from the `ModLoader` or `ModLoaderStore` classes). Instead, we have introduced new methods in [`ModLoaderMod`](../api/ModLoaderMod.md) to access these variables, such as [`ModLoaderMod.get_unpacked_dir()`](../api/ModLoaderMod.md?id=get_unpacked_dir) and [`ModLoaderMod.get_mod_data_all()`](../api/ModLoaderMod.md?id=get_mod_data_all).

### Configs
* The value for `compatible_mod_loader_version` no longer accepts a string. It needs to be passed an array instead.
* The `config_defaults` field in manifest.json has been removed. It is no longer used for specifying default configuration values.
* A new field called `config_schema` has been introduced in manifest.json. This field allows you to specify a JSONSchema for your Mod Configuration. JSONSchema provides a way to define the structure and validation rules for your configuration.

???+ note 
      There is currently no fallback mechanism for migrating old configurations to the new system. You will need to update your mod to adapt to the new configuration structure.

### Others
* Fixed a bug in the `mod_id` validation where it was possible to create a `mod_id` with fewer than 7 characters.
* Changed the mod config directory from `res://` to `user://`.

### Deprecated
Here's a list of every method and variable that is deprecated in v6. You can use a search & replace to update the old methods in your mod.

#### Setup
| Old (Search)                                   | New (Replace)                                     |
|------------------------------------------------|---------------------------------------------------|
| `ModLoader.add_translation_from_resource`      | `ModLoaderMod.add_translation`                    |
| `ModLoader.append_node_in_scene`               | `ModLoaderMod.append_node_in_scene`               |
| `ModLoader.get_mod_config`                     | `ModLoaderConfig.get_config`                      |
| `ModLoader.install_script_extension`           | `ModLoaderMod.install_script_extension`           |
| `ModLoader.mod_data`                           | `ModLoaderMod.get_mod_data_all()`                 |
| `ModLoader.register_global_classes_from_array` | `ModLoaderMod.register_global_classes_from_array` |
| `ModLoader.save_scene`                         | `ModLoaderMod.save_scene`                         |
| `ModLoader.UNPACKED_DIR`                       | `ModLoaderMod.get_unpacked_dir()`                 |

#### Logging
???+ note 
     Running a search & replace from `ModLoaderUtils.log_` to `ModLoaderLog.` will fix all of these at once.

| Old (Search)                          | New (Replace)                   |
|---------------------------------------|---------------------------------|
| `ModLoaderUtils.log_debug_json_print` | `ModLoaderLog.debug_json_print` |
| `ModLoaderUtils.log_debug`            | `ModLoaderLog.debug`            |
| `ModLoaderUtils.log_error`            | `ModLoaderLog.error`            |
| `ModLoaderUtils.log_fatal`            | `ModLoaderLog.fatal`            |
| `ModLoaderUtils.log_info`             | `ModLoaderLog.info`             |
| `ModLoaderUtils.log_success`          | `ModLoaderLog.success`          |
| `ModLoaderUtils.log_warning`          | `ModLoaderLog.warning`          |

## [v5.0.1](https://github.com/GodotModding/godot-mod-loader/releases/tag/v5.0.1)
New validation may make existing mods invalid:
* [#71](https://github.com/GodotModding/godot-mod-loader/pull/71) - Disallow leading zeros and overly long versions
* [#91](https://github.com/GodotModding/godot-mod-loader/pull/91) - Mod IDs listed in a mod manifest's `dependencies` and `incompatibilities` are now validated

## [v4.0.0](https://github.com/GodotModding/godot-mod-loader/releases/tag/v4.0.0)
* ModLoader has been moved to the `res://addons/` directory.
  * The new location is autoloaded in the same way the old one was, with the same file (*mod_loader.gd*).
  * Nothing else needs to change in your autoloads. There are other new classes, but they'll be loaded automatically.
* Logging in mods is now handled via the ModLoaderUtils class, which provides a host of new logging options.

### Renamed Methods
| Old (Search)        | New (Replace)              |
|---------------------|----------------------------|
| `ModLoader.mod_log` | `ModLoaderUtils.log_info`  |
| `ModLoader.dev_log` | `ModLoaderUtils.log_debug` |

## [v3.1.0](https://github.com/GodotModding/godot-mod-loader/releases/tag/v3.1.0)
* All funcs have been converted to snake_case (see table below, and PR [#32](https://github.com/GodotModding/godot-mod-loader/pull/32) for more info)
* meta.json is renamed to manifest.json, and its required keys have changed
  * See the example manifest.json for the current structure.
  * See also: `REQUIRED_MANIFEST_KEYS_ROOT` and `REQUIRED_MANIFEST_KEYS_EXTRA` in `mod_manifest.gd`


### Renamed Methods
| Old (Search)                 | New (Replace)                   |
|------------------------------|---------------------------------|
| `installScriptExtension`     | `install_script_extension`      |
| `addTranslationFromResource` | `add_translation_from_resource` |
| `appendNodeInScene`          | `append_node_in_scene`          |
| `saveScene`                  | `save_scene`                    |

## [v3.0.0](https://github.com/GodotModding/godot-mod-loader/releases/tag/v3.0.0)
* Two files have been renamed:
  * `ModMain.gd` -> `mod_main.gd`
  * `_meta.json` -> `manifest.json`
* The structure of the manifest JSON has changed.
  * See [README.md](https://github.com/GodotModding/godot-mod-loader/blob/main/README.md#example-manifestjson) for an example.
  * This file was previously named `_meta.json`
