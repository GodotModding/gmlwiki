# What is the Godot Mod Loader?
GML is a generalized mod loader for GDScript-based Godot games.
The mod loader allows users to create mods for games and distribute them as zips.

Importantly, it provides methods to change existing scripts, scenes, and resources without modifying and distributing vanilla game files.

???+ note
    Please note that GML does not condone the use of malicious mods. e.g. mods that allow for cheating in online games, among other things.

## Download

=== "Godot 4"

    Mod Loader: [GitHub](https://github.com/GodotModding/godot-mod-loader/tree/4.x)

    Mod Dev Tool: [GitHub](https://github.com/GodotModding/godot-mod-tool/tree/4.x)

=== "Godot 3"

    Mod Loader: [Asset Lib](https://godotengine.org/asset-library/asset/1938), [GitHub](https://github.com/GodotModding/godot-mod-loader)

    Mod Dev Tool: [Asset Lib](https://godotengine.org/asset-library/asset/1982), [GitHub](https://github.com/GodotModding/godot-mod-tool)

All stable Mod Loader versions: [GitHub Releases](https://github.com/GodotModding/godot-mod-loader/releases)
All stable Mod Dev Tool versions: [GitHub Releases](https://github.com/GodotModding/godot-mod-tool/releases)


## Mod Developer
1. [Decompile the Game](guides/modding/tools/decompile_games.md)
2. Depending on the resulting log, install [Godot](https://godotengine.org/download/) or [GodotSteam](guides/modding/tools/godot_steam.md) (mandatory if the game has Steam support)
3. [Set up](guides/integration/godot_project_setup.md) your Godot project for modding
4. Create your [Mod Structure](guides/modding/mod_structure.md)
5. Create your [Mod Files](guides/modding/mod_files.md)
6. Use the [API Methods](api/mod_loader_api.md)

## Mod user
Check if the Godot ModLoader is already integrated into the game you want to mod.
If this is not the case then [set up the Godot ModLoader](guides/integration/mod_loader_self_setup.md)

## Game Developer
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
