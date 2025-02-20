---
description: All Supported Command Line Arguments
---

# CLI Args
## Supported Command Line Arguments
| Arg                                                      | Info                                                                     |
|----------------------------------------------------------|--------------------------------------------------------------------------|
| `--mods-path="path/to/mod/zips"`                         | Override the path to the mod ZIPs dir. Default path is res://mods        |
| `--configs-path="path/to/mod/configs"`                   | Override the path to the config JSONs dir. Default path is res://configs |
| `--disable-mods`                                         | Mods will not be loaded.                                                 |
| `-vvv` / `--log-debug`                                   | Set the log verbosity to debug - log everything.                         |
| `-vv` / `--log-info`                                     | Set the log verbosity to info - log everything except debug logs.        |
| `-v` / `--log-warning`                                   | Set the log verbosity to warning - only log errors and warnings.         |
| `--log-ignore="namespace0-modname0,namespace1-modname1"` | Ignores specific mod IDs when logging                                    |

## Arguments Related to GML setup
| Arg                                              | Info                                                                                                        |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `--script addons/mod_loader/mod_loader_setup.gd` | Use this startup flag to enable the self setup.                                                             |
| `--only-setup`                                   | Allows to setup the mod loader without user notification, or auto restart.                                  |
| `--setup-create-override-cfg`                    | Forces the setup to create the override.cfg in the game base directory. Skips the project.binary injection. |

You can use these in the Godot editor via *Project > Project Settings > Display > Editor > Main Run Args*