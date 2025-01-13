---
status: new
---

# Script Hooks

!!! inline end abstract "Available since" 
    7.0.0

It works by adding callables before and after vanilla functions are called. 

[API reference: `#!gd ModLoaderMod.install_script_extension()`](../../api/mod_loader_mod.md#method-install_script_extension)

how it works
- dynamic
- preprocessed/ built in

## What Script Hooks __can__ do

mod class name scripts
extend before and after 
replace (don't call super) (careful, this makes your mod less compatible since it breaks the chain of modded methods)


## What Script Hooks can __not__ do

less efficient

not in godot 3

can't add new member vars or funcs

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

