# Script Extensions
## Overriding Virtual Functions in Script Extensions
Virtual functions are functions like `_ready()` or `_init()`. They are used to execute code at specific "events" or "notifications". You can learn more about them in the [Godot Docs](https://docs.godotengine.org/en/3.5/tutorials/scripting/overridable_functions.html).

?> For modding, it is important to know that you can't override these functions in a script extension.

Here's how the `_ready()` function works:
1. It initializes the parent `onready` variable.
2. It executes the parent Base's `_ready()` function.
3. It initializes the child's `onready` variable.
4. It executes the child's `_ready()` function.

[Related GitHub Issue](https://github.com/godotengine/godot/issues/33620#issuecomment-553912225)

This is why it's not advisable to call the parent `.ready()` function in a script extension, as doing so would result in its execution being duplicated.

[This behavior changed in Godot 4.x with the introduction of the super keyword.](https://docs.godotengine.org/en/latest/tutorials/scripting/gdscript/gdscript_basics.html#inheritance)


## Script Inheritance
?> This info comes from the docs for the [Delta-V mod loader](https://gitlab.com/Delta-V-Modding/Mods/-/blob/main/MODDING.md) for a full write up check this [blog post](https://blog.cy.md/2022/05/27/modding-for-godot/).

In order to allow modifying game functions without copying the contents of the functions or entire scripts in mod code, this system makes use of inheritance for hooking. We exploit the fact that all Godot scripts are also classes and may extend other scripts in the same way how a class may extend another class; this allows mods to include script extensions, which extend some standard game script and selectively override some methods.

For example, this simple script extension changes the path that save files are loaded from in the game Brotato.

The location of this example script extension would be here: `res://mods-unpacked/Author-ModName/extensions/singletons/progress_data.gd`

```gdscript
# Our base script is the original game script.
extends "res://singletons/progress_data.gd"

# This overrides the method with the same name, changing the value of its argument:
func load_game_file(path:String = SAVE_PATH)->void:
	var modded_path = path + "--modded.json"

	# Calling the base method will call the original game method:
	.load_game_file(modded_path)
        # Godot 4 uses the super() method instead of prefixing the original method with a .

	# Note that if the vanilla script returned something, we would do this instead:
	#return .load_game_file(modded_path)
```

To install it, call [ModLoaderMod.install_script_extension]() from your mod's `mod_main.gd`, in `_init`:

```gdscript
extends Node

func _init():
	ModLoaderMod.install_script_extension('res://mods-unpacked/Author-ModName/extensions/singletons/progress_data.gd')
```


## Inheritance chaining
To allow multiple mods to customize the same base script, `install_script_extension` takes care of inheritance chaining. In practice, this is transparent to mods, and in theory things should "just work".