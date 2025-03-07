---
description: Small class to keep the state of hook execution chains and move between mod hook calls.
---

# ModLoaderHookChain
**Inherits**: RefCounted


Small class to keep the state of hook execution chains and move between mod hook calls.  
For examples, see [`#!gd ModLoaderMod.add_hook()`](mod_loader_mod.md#method-add_hook).
<hr style="border-width: thick">

## Constants
#### • `#!gd LOG_NAME`: `#!gd "ModLoaderHookChain"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 

<hr style="border-width: thick">

## Properties
#### • `#!gd reference_object` {#property-reference_object data-toc-label='reference_object'} 

<hr style="border-width: thick">

## Method Descriptions
### • [`#!gd Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html) <code class="highlight">execute_next(args: [Array](https://docs.godotengine.org/en/stable/classes/class_array.html))</code> {#method-execute_next data-toc-label='execute_next'}
#### Description:
Will execute the next mod hook callable or vanilla method and return the result.

  
#### Parameters:
  
- `#!gd args` ([`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of all arguments passed into the vanilla function. 

  
**Returns:**
  
- [`#!gd Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html): Return value of the next function in the chain.

Make sure to call this method *<span style="color: orange">once</span>* somewhere in the `#!gd mod_callable` you pass to [`#!gd ModLoaderMod.add_hook()`](mod_loader_mod.md#method-add_hook).   

***
### • [`#!gd Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html) <code class="highlight">execute_next_async(args: [Array](https://docs.godotengine.org/en/stable/classes/class_array.html))</code> {#method-execute_next_async data-toc-label='execute_next_async'}
#### Description:
Same as [`#!gd execute_next()`](#method-execute_next), but asynchronous - it can be used if a method uses `#!gd await`. 

  
#### Parameters:
  
- `#!gd args` ([`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of all arguments passed into the vanilla function. 

  
**Returns:**
  
- [`#!gd Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html): Return value of the next function in the chain.

This hook needs to be used if the vanilla method uses `#!gd await` somewhere.   
Make sure to call this method *<span style="color: orange">once</span>* somewhere in the `#!gd mod_callable` you pass to [`#!gd ModLoaderMod.add_hook()`](mod_loader_mod.md#method-add_hook).   

***
