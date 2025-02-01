---
status: new
---

# Script Hooks

!!! inline end abstract "Available since" 
    7.0.0


Script Hooks are a new way to mod scripts. Hooks allow you to add a custom [Callable](https://docs.godotengine.org/en/stable/classes/class_callable.html),
which then calls further modded functions and the vanilla function at the end. The callable needs to fulfil specific 
requirements to work.

Hooks are slightly more complex to use and little less powerful than [Script Extensions](script_extensions.md), 
so prefer using those if possible.

!!! info
    The Mod Loader makes Script Hooks work by generating new GDScript files, which take the place of the original vanilla 
    scripts. The newly generated scripts then use the [ModLoaderHookChain](../../api/mod_loader_hook_chain.md) to call 
    modded callables one after the other. These callables need to always take the chain as first argument and also call 
    [`#!gd ModLoaderHookChain.execute_next()`](../../api/mod_loader_hook_chain.md#method-execute_next) once at some point
    to properly work.

There are two ways in which mod hooks can take the place of vanilla scripts:

1. Dynamic
    - This does not work in the editor! See [Hooks in the Editor](#hooks-in-the-editor) below.
    - Generated at runtime by the mod loader. This is automatic, you don't have to do anything.
    - Any file can technically be converted, but the hook file can't be applied if the script is preloaded. 
2. Preprocessed/ built in
    - These are created during export if the game developer has enabled the Mod Hook preprocessor export addon.
    - You can always hook a preprocessed file, preloaded or not. 
    - You can check if a file has a comment similar to this *"ModLoader Hooks - The following code has been automatically 
        added by the Godot Mod Loader."* to see if it is already hooked.

## Features

The main feature of mod hooks is that they can mod global classes - scripts which use `class_name` to be globally accessible.
Global classes have a bug which prevents us from using extensions.

Hooks can modify member variables by accessing the [`#!gd ModLoaderHookChain.reference_object`](../../api/mod_loader_hook_chain.md#property-reference_object). 
Example: this hook method that is attached to the main node which contains the game's version.

=== "Godot 4"
    ```gdscript
    func change_version(chain: ModLoaderHookChain) -> void:
        # Using a typecast here (with "as") can help with autocomplete and avoiding errors
        var main_node := chain.reference_object as MainGame
        main_node.version = "Modloader Hooked!"
        # _ready, which we are hooking, does not have any arguments
        chain.execute_next()
    ```

=== "Godot 3"
    !!! warning
        This feature does not exist in Godot 3

Similarly to extensions, hooks can also change vanilla methods before and after they are called, which allows them to 
manipulate both the input parameters and the output value of a function.  

=== "Godot 4"
    ```gdscript
    # Parameters can be manipulated easily by changing what is passed into .execute_next()
    # The vanilla method (Utilities.format_date) takes 3 arguments, our hook method takes
    # the ModLoaderHookChain followed by the same 3
    func time_travel(chain: ModLoaderHookChain, day: int, month: int, year: int) -> String:
        print("time travel!")
        year -= 100
        # Just the vanilla arguments are passed along in the same order, wrapped into an Array
        var val = chain.execute_next([day, month, year])
        return val
    
    
    # The return value can be manipulated by calling the next hook (or vanilla) first
    # then changing it and returning the new value.
    func add_season(chain: ModLoaderHookChain, day: int, month: int, year: int) -> String:
        var output = chain.execute_next([day, month, year])
        match month:
            12, 1, 2:
                output += ", Winter"
            3, 4, 5:
                output += ", Spring"
            6, 7, 8:
                output += ", Summer"
            9, 10, 11:
                output += ", Autumn"
        return output
    ```

=== "Godot 3"
    !!! warning
        This feature does not exist in Godot 3


As you may have noticed above, each one of the mod hook functions calls `#!gd chain.execute_next()`. This is almost like
calling `super()` in a script extension - it hands off the call to the next modded, or finally the vanilla method.

That means you can also completely replace the vanilla method by never calling `#!gd chain.execute_next()` - but be careful
with this as it will likely break all compatibility with other mods that try to hook the same method.

Hooks can be applied to Autoloads, but you should really prefer extensions since Autoloads can't have class_names either way.
It may be possible to hook autoloads earlier in the load order, but this hasn't been tested. Do note that in case it works
it is impossible the stop the Autoload's _init from running since hooks are applied during the ModLoader's _ready

## Limitations

Script Hooks don't exist for Godot 3, they are a recent addition. They are also not required in 3 since even global classes can
be modded with Script extensions in Godot 3.

Script Hooks suffer from the same limitation that Extensions do, they will not be applied to scripts that are 
[`preload()`ed](https://docs.godotengine.org/en/stable/classes/class_%40gdscript.html#class-gdscript-method-preload "preload() is a GDScript feature") 
in any way. This affects both scripts which are preloaded directly - `#!gd preload("res://player.gd")` - and scripts which are
indirectly preloaded by being used in preloaded scenes - `#!gd preload("res://player.tscn")`.   
This is a Godot limitation we have yet to find a workaround for.

Hooks can only access the reference object indirectly to change values, which means they cannot add new variables to the 
class they are applied to.

Subclasses (declared with `#!gd class` inside another class) can't be modded yet. Simply because we didn't add that 
feature to the hook preprocessor yet since it's rarely used and was not needed yet. If you need support for this, please 
let us know on this [issue #516](https://github.com/GodotModding/godot-mod-loader/issues/516)

There is technically a small hit to performance when using hooks compared to extensions, but it is negligible in most cases.

## Hooks in the editor

The dynamically generated script that our mod hook preprocessor creates cannot be applied in the editor 
([at least until 4.4](https://github.com/godotengine/godot/pull/90425)).  
To work around this issue, you can use the [mod tool file system context menu](tools/mod_tool.md#file-system-context-menu)
and convert the vanilla file once. Afterward you will be able to test mod hooks as if there were no differences.

## Usage

!!! abstract "See also" 
    [API Reference: `#!gd ModLoaderMod.add_hook()`](../../api/mod_loader_mod.md#method-add_hook) and  
    [API Reference: `#!gd ModLoaderMod.install_script_hooks()`](../../api/mod_loader_mod.md#method-install_script_hooks)

one by one
ModLoaderMod.add_hook()

???+ note
    While a single script extension extends a whole file (even if it only changes one method), a single script hook only 
    affects a single method. For convenience, we added an "install-" method which applies all hooks from a file. 

ModLoaderMod.install_script_hooks()

=== "Godot 4"

=== "Godot 3"
    !!! warning
        This feature does not exist in Godot 3

### Hook method

!!! bug "Common issues"
    1. Always make sure you are calling `#!gd chain.execute_next()`!
    2. [In editor](#hooks-in-the-editor): Make sure the file is converted!

