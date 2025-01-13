---
status: new
---

# Script Extensions

Script extensions are the preferred way to change, extend and replace behaviour of an existing vanilla script.

It works by registering an entire file of new script functions as a child script of a vanilla script. Not all methods 
from the original script need to be in the extension script.

[API reference: `#!gd ModLoaderMod.install_script_extension()`](../../api/mod_loader_mod.md#method-install_script_extension)

## What Script Extensions __can__ do

Script extensions can

[//]: # (TODO)
extend before and after (call parent method with super() or `.`, except for virtuals in 3)
replace (don't call super) (careful, this makes your mod less compatible since it breaks the chain of modded methods)

!!! note
    Since Godot 4 it is possible to completely replace virtual functions if the 
    [`super`](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#inheritance) 
    keyword is not used within the function.

add member vars and funcs

## What Script Extensions can __not__ do

Script Extensions will not be applied to scripts that are 
[`preload()`ed](https://docs.godotengine.org/en/stable/classes/class_%40gdscript.html#class-gdscript-method-preload "preload() is a GDScript feature") 
in any way. This affects both scripts which are preloaded directly - `#!gd preload("res://player.gd")` - and scripts which are
indirectly preloaded by being used in preloaded scenes - `#!gd preload("res://player.tscn")`.   
This is a Godot limitation we have yet to find a workaround for.

some scenes can be worked around by modding the scene that instantiates them
- like the pause menu in dome keeper which was preloaded and instantiated - changed the menu after it was created

[//]: # (TODO)
Redefine member variables
- use a function like ready init or the one you are using it in to change their value

change constants unless they are arrays/dictionaries (just values)

insert code in the middle of functions (ask dev if they can split it)

=== "Godot 4"
    Extending global classes (scripts with `class_name` at the top) is not possible. 
    To work around this issue, we've created [Script Hooks](script_hooks.md), use them instead of 
    extensions when necessary.

    !!! bug "Related Godot Issue"
        [#83542](https://github.com/godotengine/godot/issues/83542)

=== "Godot 3"

    It is not possible to replace [virtual functions](https://docs.godotengine.org/en/3.5/tutorials/scripting/overridable_functions.html) 
    with a script extension, since the function from the parent class will always be called by Godot.
    Because of this, using `._ready()` - the `_ready()` function of the parent class - in a script extension will result 
    in that function being called twice.

    ???+ info
        Virtual functions, like `_ready()` or `_init()`, are used to execute code when specific "events", also called 
        "notifications", occur. You can learn more about them in the 
        [Godot Documentation](https://docs.godotengine.org/en/3.5/tutorials/scripting/overridable_functions.html).

    !!! bug "Related Godot Issue"
        [#33620](https://github.com/godotengine/godot/issues/33620#issuecomment-553912225)

## Usage

This script extension changes the path that save files are loaded from in the game Brotato.

The location of this example script extension would be here: 
`res://mods-unpacked/Author-ModName/extensions/singletons/progress_data.gd`

=== "Godot 4"

    ```gdscript
    # Our base script is the original game script.
    extends "res://singletons/progress_data.gd"
    
    # This overrides the method with the same name, changing the value of its argument:
    func load_game_file(path: String = SAVE_PATH) -> void:
        var modded_path = path + "--modded.json"
    
        # Calling the base method will call the original game method:
        super(modded_path)
    
        # Note that if the vanilla script returned something, we would do this instead:
        #return super(modded_path)
    ```

=== "Godot 3"

    ```gdscript
    # Our base script is the original game script.
    extends "res://singletons/progress_data.gd"
    
    # This overrides the method with the same name, changing the value of its argument:
    func load_game_file(path: String = SAVE_PATH) -> void:
        var modded_path = path + "--modded.json"
    
        # Calling the base method will call the original game method:
        .load_game_file(modded_path)
    
        # Note that if the vanilla script returned something, we would do this instead:
        #return .load_game_file(modded_path)
    ```

To install it, call [ModLoaderMod.install_script_extension]() from your mod's `mod_main.gd`, in `_init`:

=== "Godot 4"

    ```gdscript
    extends Node

    func _init():
        ModLoaderMod.install_script_extension('res://mods-unpacked/Author-ModName/extensions/singletons/progress_data.gd')
    ```

=== "Godot 3"

    ```gdscript
    extends Node

    func _init():
        ModLoaderMod.install_script_extension('res://mods-unpacked/Author-ModName/extensions/singletons/progress_data.gd')
    ```

## Technical Details

### Script Inheritance
!!! info 
     This info comes from the docs for the [Delta-V mod loader](https://gitlab.com/Delta-V-Modding/Mods/-/blob/main/MODDING.md) for a full write-up check this [blog post](https://blog.cy.md/2022/05/27/modding-for-godot/).

In order to allow modifying game functions without copying the contents of the functions or entire scripts in mod code, 
this system makes use of inheritance for hooking. We exploit the fact that all Godot scripts are also classes and may 
extend other scripts in the same way how a class may extend another class; this allows mods to include script extensions, 
which extend some standard game script and selectively override some methods.

### Inheritance chaining
By using `install_script_extension`, the Mod Loader builds a chain of scripts which are applied one by one. 
The order of the chain is determined by the [`manifest.json`](mod_files.md#manifestjson) fields 
`dependencies`, `optional_dependencies` and `load_before`. 

If these fields are set correctly, multiple mods should "just work" together without any additional work.
