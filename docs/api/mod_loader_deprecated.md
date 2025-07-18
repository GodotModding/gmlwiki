---
description: API methods for deprecating funcs. Can be used by mods with public APIs.
---

# ModLoaderDeprecated
**Inherits**: Object


API methods for deprecating funcs. Can be used by mods with public APIs.
<hr style="border-width: thick">

## Constants
#### • `#!gd2 LOG_NAME`: `#!gd2 "ModLoader:Deprecated"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 

<hr style="border-width: thick">

## Method Descriptions
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 deprecated_changed(` `#!gd2 old_method:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 new_method:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 since_version:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 show_removal_note:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-deprecated_changed data-toc-label='deprecated_changed' .no-code-padding}
#### Description:
Marks a method that has changed its name or class.

#### Parameters:
  
- `#!gd2 old_method` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the deprecated method.  
- `#!gd2 new_method` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the new method to use.  
- `#!gd2 since_version` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The version number from which the method has been deprecated.  
- `#!gd2 show_removal_note` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (optional) If true, includes a note about future removal of the old method. Default is true.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 deprecated_removed(` `#!gd2 old_method:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 since_version:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 show_removal_note:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-deprecated_removed data-toc-label='deprecated_removed' .no-code-padding}
#### Description:
Marks a method that has been entirely removed, with no replacement.

#### Parameters:
  
- `#!gd2 old_method` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the removed method.  
- `#!gd2 since_version` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The version number from which the method has been deprecated.  
- `#!gd2 show_removal_note` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (optional) If true, includes a note about future removal of the old method. Default is true.

**Returns:**
  
- No return value



!!! note 
	This should rarely be needed but is included for completeness.
  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 deprecated_message(` `#!gd2 msg:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 since_version:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-deprecated_message data-toc-label='deprecated_message' .no-code-padding}
#### Description:
Marks a method with a freeform deprecation message.

#### Parameters:
  
- `#!gd2 msg` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The deprecation message.  
- `#!gd2 since_version` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): (optional) The version number from which the deprecation applies.

**Returns:**
  
- No return value  

***
