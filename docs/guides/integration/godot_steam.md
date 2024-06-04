# GodotSteam
The standard version of Godot doesn't have native support for the Steam SDK. This means that, if the game you're editing has Steam support, it probably won't run. To solve this, use a modified version of the Godot editor called [GodotSteam](https://github.com/Gramps/GodotSteam).

You'll want to get the [GodotSteam release](https://github.com/Gramps/GodotSteam/releases) version that matches your game's version (eg. Godot 3.5 is [here](https://github.com/Gramps/GodotSteam/releases/tag/g35-s155-gs3174)). Also note that GodotSteam comes as a GDNative plugin version, but you want the full pre-compiled editor.

Make sure you read GodotSteam's [docs on exporting](https://gramps.github.io/GodotSteam/tutorials-exporting-shipping.html), because there are some limitations and caveats -- eg. you need to set up your export templates manually, and can't use the "Export with Debug" option.