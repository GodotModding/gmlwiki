---
description: Most games released on Steam use GodotSteam learn why you need it for modding.
---

# GodotSteam
The standard version of Godot doesn't have native support for the Steam SDK. This means that, if the game you're editing
has Steam support, it probably won't run. To solve this, use a modified version of the Godot editor called [GodotSteam](https://github.com/Gramps/GodotSteam).

You'll want to get the [GodotSteam release](https://github.com/Gramps/GodotSteam/releases) version that matches your game's version (eg. Godot 3.5 is [here](https://github.com/Gramps/GodotSteam/releases/tag/g35-s155-gs3174)). 
Also note that GodotSteam comes as a GDNative/GDExtension plugin version - both work, but the full pre-compiled editor 
is simpler to get running.

You will usually be able to get the Godot version from the [gdre export log](decompile_games.md), and you can usually 
take the newest GodotSteam version that supports it. To get the exact version you will usually have to
ask the game developer - and sometimes the modding guide for each game will tell you.
