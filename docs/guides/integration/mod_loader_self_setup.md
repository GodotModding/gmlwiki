# Mod Loader Self Setup
If the game you want to mod does not natively use this ModLoader, you will have to complete a few steps to set it up:

1. Download the [latest release](https://github.com/GodotModding/godot-mod-loader/releases) of the ModLoader
2. Place the `/addons` folder from the ModLoader next to the executable of the game you want to mod.
3. Set this flag `--script addons/mod_loader/mod_loader_setup.gd`
    - **Steam:** right-click the game in the game list > press properties > enter the flag in startup options
- **Other:** search for "set launch (or command line) parameters [your platform]"

If the game window shows `(Modded)` in the title, setup was successful.

It is possible to add additional setup arguments, but only do so if a game-specific setup documentation advises it. [More install arguments here](cli_args.md).

# A deeper look
The ModLoader comes with a helper script to properly install itself without having to recompile a game's source. There are two options to make this work:
- **Inject a custom `project.binary` file into the games main `.pck`**
    To do this, [GodotPckTool](https://github.com/hhyyrylainen/GodotPckTool) is used.
    This approach is currently only supported on Windows and with games that have a .pck file that is not embedded.
    Using this method allows us to add the ModLoader at the top of the autoload chain.
    This is important, because it allows mods to add [Script Extensions](docs/api/ModLoaderMod.md#install_script_extension) to autoloads.

- **Use Godot's `override.cfg` functionality to override the game project settings**
    This is the ideal solution if mods for a game don't require extensions of autoloads.
    It uses the built-in way to override project settings via an `override.cfg` in the game directory.
    If you prefer this method or are using an operating system that doesn't support the binary injection yet,
    you can set this CLI argument `--setup-create-override-cfg`.
    For more details check Godot's [ProjectSettings Docs](https://docs.godotengine.org/en/3.5/classes/class_projectsettings.html#class-projectsettings) at Overriding

We hope to only use the `override.cfg` in the future - *that's why we opened a [feature proposal](https://github.com/godotengine/godot-proposals/discussions/6137) that allows the overriding of the autoload order*.
Please consider upvoting this proposal so modding becomes easier for everyone :)

# Folder locations
**Game Executable:**
Right-click the game in Steam > Click Manage > Browse Local Files. This will open the game's folder.

*Note: For MacOS, you are also at the right place even though the actual executable is in `/Contents/MacOS` within that folder. The override.cfg will be placed there, everything else (like the mods folder) goes right here.*

**User Data:**
- **Windows:** `%appdata%\Godot\app_userdata\<game name>`
- **Linux:** `~/.local/share/godot/app_userdata/<game name>`
- **Mac:** `~/Library/Application Support/Godot/app_userdata/<game name>`
