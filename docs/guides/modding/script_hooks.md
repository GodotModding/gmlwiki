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

[API reference: `#!gd ModLoaderMod.install_script_hooks()`](../../api/mod_loader_mod.md#method-install_script_hooks)

The Mod Loader makes Script Hooks work by dynamically generating GDScript files, which replace the  

- dynamic
- preprocessed/ built in

## Features

mod class name scripts
extend before and after 
replace (don't call super) (careful, this makes your mod less compatible since it breaks the chain of modded methods)


## Limitations

less efficient

not in godot 3

can't add new member vars or funcs to the original class

## Hooks in the editor

original vanilla scripts need to be converted
- [mod tool](tools/mod_tool.md)

## Usage

ModLoaderMod.install ..

or one by one

ModLoaderMod.

### Hook method

!!! bug "Common issues"
    1. Always make sure you are calling `#!gd chain.execute_next()`!
    2. [In editor](#hooks-in-the-editor): Make sure the file is converted!

