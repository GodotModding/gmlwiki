---
description: Small class to keep the state of hook execution chains and move between mod hook calls.
---

# ModLoaderHookChain
**Inherits**: RefCounted


Small class to keep the state of hook execution chains and move between mod hook calls.  
For examples, see [`#!gd2 ModLoaderMod.add_hook()`](mod_loader_mod.md#method-add_hook).
<hr style="border-width: thick">

## Constants
#### • `#!gd2 LOG_NAME`: `#!gd2 "ModLoaderHookChain"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 

<hr style="border-width: thick">

## Properties
#### • `#!gd2 reference_object` {#property-reference_object data-toc-label='reference_object'} 

<hr style="border-width: thick">

## Method Descriptions
### • [`#!gd2 Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html)&nbsp;&nbsp;`#!gd2 execute_next(` `#!gd2 args:`&nbsp;&nbsp;[`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)`#!gd2 ) ` {#method-execute_next data-toc-label='execute_next' .no-code-padding}
#### Description:
Will execute the next mod hook callable or vanilla method and return the result.

  
#### Parameters:
  
- `#!gd2 args` ([`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of all arguments passed into the vanilla function. 

  
**Returns:**
  
- [`#!gd2 Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html): Return value of the next function in the chain.

Make sure to call this method *<span style="color: orange">once</span>* somewhere in the `#!gd2 mod_callable` you pass to [`#!gd2 ModLoaderMod.add_hook()`](mod_loader_mod.md#method-add_hook).   

***
### • [`#!gd2 Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html)&nbsp;&nbsp;`#!gd2 execute_next_async(` `#!gd2 args:`&nbsp;&nbsp;[`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)`#!gd2 ) ` {#method-execute_next_async data-toc-label='execute_next_async' .no-code-padding}
#### Description:
Same as [`#!gd2 execute_next()`](#method-execute_next), but asynchronous - it can be used if a method uses `#!gd2 await`. 

  
#### Parameters:
  
- `#!gd2 args` ([`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of all arguments passed into the vanilla function. 

  
**Returns:**
  
- [`#!gd2 Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html): Return value of the next function in the chain.

This hook needs to be used if the vanilla method uses `#!gd2 await` somewhere.   
Make sure to call this method *<span style="color: orange">once</span>* somewhere in the `#!gd2 mod_callable` you pass to [`#!gd2 ModLoaderMod.add_hook()`](mod_loader_mod.md#method-add_hook).   

***
