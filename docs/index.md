# Godot Mod Loader
***
<div align="center">
<img alt="Godot Modding Logo" src="_media/logo.png" width="256" />
</div>
***

## What is the Godot Mod Loader?
GML is a generalized mod loader for GDScript-based Godot games.
The mod loader allows users to create mods for games and distribute them as zips.

Importantly, it provides methods to change existing scripts, scenes, and resources **without** _modifying_ or _distributing_ vanilla game files.

!!! danger ""
    We, the mod loader team, do not condone using or creating malicious mods and piracy of any kind. 

## Downloads

=== "Godot 4"

    Mod Loader: [GitHub](https://github.com/GodotModding/godot-mod-loader/tree/4.x)

    Mod Dev Tool: [GitHub](https://github.com/GodotModding/godot-mod-tool/tree/4.x)

=== "Godot 3"

    Mod Loader: [Asset Lib](https://godotengine.org/asset-library/asset/1938), [GitHub](https://github.com/GodotModding/godot-mod-loader)

    Mod Dev Tool: [Asset Lib](https://godotengine.org/asset-library/asset/1982), [GitHub](https://github.com/GodotModding/godot-mod-tool)

All stable **Mod Loader** versions: [GitHub Releases](https://github.com/GodotModding/godot-mod-loader/releases)  
All stable **Mod Dev Tool** versions: [GitHub Releases](https://github.com/GodotModding/godot-mod-tool/releases)

***

## Getting started

Depending on what your goals are, setup of the mod loader will be slightly different.

As a [mod user](#mod-user), you usually don't have to do much at all. If you are lucky the game already has the mod loader
integrated, and you just need to add your mods. If not, the self setup is only a download and placing files in the correct spot.

As a [game developer](#game-developer) wishing to integrate the Mod Loader natively, you will only have to install it and add two autoloads.
You can optionally configure a few aspects through the [options](guides/integration/mod_loader_options.md).

As a [mod developer](#mod-developer), it is recommended that you work on your mods with access to the vanilla source code. 
Some games provide it, but for most, [decompiling the game](guides/modding/tools/decompile_games.md) will be necessary. 
There are several steps on the path of creating a mod to finally uploading it, but there are tools like the [Mod Dev Tool](guides/modding/tools/mod_tool.md)
and [Steam Workshop Uploader](guides/modding/tools/workshop_uploader.md) to help you along the way.

### Mod Developer

It is recommended that you know a little bit about the [Godot](https://docs.godotengine.org/en/stable/about/introduction.html#about-godot-engine) 
game engine. You will be creating mods using the built-in scripting language [GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#doc-gdscript) 
and distributing them as ZIPs. 

??? tip "Learn GDScript"
    Here is a starter on the language: [overview](https://docs.godotengine.org/en/4.2/tutorials/scripting/gdscript/index.html) 
    and [language basics](https://docs.godotengine.org/en/4.2/tutorials/scripting/gdscript/gdscript_basics.html)  
    if you are a total beginner and like interactive courses, you can use [Learn GDScript from Zero](https://docs.godotengine.org/en/stable/getting_started/introduction/learn_to_code_with_gdscript.html) by GDQuest. 
    It's aimed at absolute beginners, so if you already know a programming language it might be a bit slow for you.  
    And if you prefer videos you can watch the [How to program in Godot - GDScript Tutorial](https://www.youtube.com/watch?v=e1zJS31tr88) by Brackey's

???+ Note
    Several games already have the Mod Loader integrated and some have specific help pages with game-specific information.
    
    - Dome Keeper: [DomeKeeperMods Wiki](https://github.com/DomeKeeperMods/Docs/wiki)
    - Brotato: [Steam Workshop Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2931079751)
    - Windowkill: [Developer website](https://torcado.com/windowkill/mods/modding.html)
    - Megaloot
    - Endoparasitic
    - Of Life and Land

1. [Decompile the Game](guides/modding/tools/decompile_games.md) (if the source code is not provided)
2. Install [Godot](https://godotengine.org/download/) or [GodotSteam](guides/modding/tools/godot_steam.md)
    - The decompilation log will tell you if it's default Godot or a custom build, in which case it's likely to be GodotSteam.
        In some cases (like Windowkill) it's a completely custom engine version which may be provided by the developer.
    - GodotSteam is mandatory if the game has Steam support like achievements or leaderboards
3. [Set up](guides/integration/godot_project_setup.md) your Godot project for modding (if the mod loader is not integrated yet)
4. Create your [Mod Structure](guides/modding/mod_structure.md)
5. Create your [Mod Files](guides/modding/mod_files.md)
6. Use the [API Methods](api/mod_loader_api.md)
7. Easily [Test and debug](guides/modding/testing_debugging.md) your mod

### Mod user
Check if the Godot ModLoader is already integrated into the game you want to mod.
If this is not the case then [use the self setup](guides/integration/mod_loader_self_setup.md)

### Game Developer
[Add the Godot ModLoader to your project](guides/integration/godot_project_setup.md), feel free to join our [Discord](https://discord.gg/J5AvdFK4mw) for any support!

# Versions & Releases
- [Breaking Changes](misc/breaking_changes.md)
- [Upcoming Features](misc/upcoming_features.md)

# Credits
The Godot ModLoader is based on the brilliant work done for [Delta-V-Modding](https://gitlab.com/Delta-V-Modding/Mods).

The core developers of GML are: [KANA](https://github.com/KANAjetzt), [Darkly77](https://github.com/ithinkandicode), [Ste](https://github.com/Qubus0), and [otDan](https://github.com/otDan).

<br></br>

---

<div align="center">
  <b>GML is possible thanks to all these wonderful people</b>
  <br></br>
  <a href="https://github.com/GodotModding/godot-mod-loader/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=GodotModding/godot-mod-loader" />
  </a>
</div>

---
