
This class provides methods for deprecating functions. Can be used by mods with public APIs.

## Methods Overview
| Method                                      | Description                                                         |
|---------------------------------------------|---------------------------------------------------------------------|
| [`deprecated_changed`](#deprecated_changed) | Marks a method that has changed its name or class.                  |
| [`deprecated_removed`](#deprecated_removed) | Marks a method that has been entirely removed, with no replacement. |
| [`deprecated_message`](#deprecated_message) | Marks a method with a freeform deprecation message.                 |

## Methods
### deprecated_changed
```gdscript
func deprecated_changed(old_method: String, new_method: String, since_version: String, show_removal_note: bool = true) -> void
```
Marks a method that has changed its name or class.

Parameters:
- old_method (String): The name of the deprecated method.
- new_method (String): The name of the new method to use.
- since_version (String): The version number from which the method has been deprecated.
- show_removal_note (bool): (optional) If true, includes a note about future removal of the old method. Default is true.


### deprecated_removed
```gdscript
func deprecated_removed(old_method: String, since_version: String, show_removal_note: bool = true) -> void
```
Marks a method that has been entirely removed, with no replacement. Note: This should rarely be needed but is included for completeness.

Parameters:
- old_method (String): The name of the removed method.
- since_version (String): The version number from which the method has been deprecated.
- show_removal_note (bool): (optional) If true, includes a note about future removal of the old method. Default is true.


### deprecated_message
```gdscript
func deprecated_message(msg: String, since_version: String = "") -> void
```
Marks a method with a freeform deprecation message.

Parameters:
- msg (String): The deprecation message.
- since_version (String): (optional) The version number from which the deprecation applies.


## Constants Descriptions
##### LOG_NAME
```gdscript
const LOG_NAME: String = "ModLoader:Deprecated"
```