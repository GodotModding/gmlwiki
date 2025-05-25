---
description: This Class provides methods for logging, retrieving logged data, and internal methods for working with log files.
---

# ModLoaderLog
**Inherits**: Object


This Class provides methods for logging, retrieving logged data, and internal methods for working with log files.
<hr style="border-width: thick">

## Constants
#### • `#!gd2 MOD_LOG_PATH`: `#!gd2 "user://logs/modloader.log"` {#constant-MOD_LOG_PATH data-toc-label='MOD_LOG_PATH'} 
#### • `#!gd2 ERROR`: `#!gd2 0` {#constant-ERROR data-toc-label='ERROR'} 
#### • `#!gd2 WARNING`: `#!gd2 1` {#constant-WARNING data-toc-label='WARNING'} 
#### • `#!gd2 INFO`: `#!gd2 2` {#constant-INFO data-toc-label='INFO'} 
#### • `#!gd2 DEBUG`: `#!gd2 3` {#constant-DEBUG data-toc-label='DEBUG'} 

<hr style="border-width: thick">

## Properties
#### • `#!gd2 logged_messages` {#property-logged_messages data-toc-label='logged_messages'} 
#### • `#!gd2 verbosity` {#property-verbosity data-toc-label='verbosity'} 
#### • `#!gd2 ignored_mods` {#property-ignored_mods data-toc-label='ignored_mods'} 
#### • `#!gd2 hint_color` {#property-hint_color data-toc-label='hint_color'} 

<hr style="border-width: thick">

## Method Descriptions
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 fatal(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-fatal data-toc-label='fatal' .no-code-padding}
#### Description:
Logs the error in red and a stack trace. Prefixed FATAL-ERROR.  
Always logged.

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as an error.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value



!!! bug "Breakpoint"
	Stops execution in the editor, use this when something really needs to be fixed.
  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 error(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-error data-toc-label='error' .no-code-padding}
#### Description:
Logs the message and pushes an error. Prefixed ERROR.  
Always logged.

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as an error.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 warning(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-warning data-toc-label='warning' .no-code-padding}
#### Description:
Logs the message and pushes a warning. Prefixed WARNING.  
Logged with verbosity level at or above warning (`#!gd2 -v` or `#!gd2 --log-warning`).

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a warning.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 info(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-info data-toc-label='info' .no-code-padding}
#### Description:
Logs the message. Prefixed INFO.  
Logged with verbosity level at or above info (`#!gd2 -vv` or `#!gd2 --log-info`).

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as an information.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 success(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-success data-toc-label='success' .no-code-padding}
#### Description:
Logs the message. Prefixed SUCCESS.  
Logged with verbosity level at or above info (`#!gd2 -vv` or `#!gd2 --log-info`).

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a success.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 debug(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-debug data-toc-label='debug' .no-code-padding}
#### Description:
Logs the message. Prefixed DEBUG.  
Logged with verbosity level at or above debug (`#!gd2 -vvv` or `#!gd2 --log-debug`).

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a debug.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 hint(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-hint data-toc-label='hint' .no-code-padding}
#### Description:
Logs the message. Prefixed HINT and highligted.  
Logged with verbosity level at or above debug (`#!gd2 -vvv` or `#!gd2 --log-debug`) and in the editor only. Not written to mod loader log.  


!!! note 
	Use this to help other developers debug issues by giving them error-specific hints.


#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a debug.  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • `#!gd2 void`&nbsp;&nbsp;`#!gd2 debug_json_print(` `#!gd2 message:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 json_printable:`&nbsp;&nbsp;[`#!gd2 Variant`](https://docs.godotengine.org/en/stable/classes/class_variant.html)`#!gd2 , ` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 only_once:`&nbsp;&nbsp;[`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)`#!gd2 ) static ` {#method-debug_json_print data-toc-label='debug_json_print' .no-code-padding}
#### Description:
Logs the message formatted with [`#!gd2 JSON.print()`](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json-method-print). Prefixed DEBUG.  
Logged with verbosity level at or above debug (`#!gd2 -vvv` or `#!gd2 --log-debug`).

#### Parameters:
  
`#!gd2 message` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a debug.  
`#!gd2 json_printable` (Variant): The variable to be formatted and printed using [`#!gd2 JSON.print()`](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json-method-print).  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd2 only_once` ([`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
  
- No return value  

***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_all_as_resource(` `#!gd2 ) static ` {#method-get_all_as_resource data-toc-label='get_all_as_resource' .no-code-padding}
#### Description:
Returns an array of log entries as a resource.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as resource.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_all_as_string(` `#!gd2 ) static ` {#method-get_all_as_string data-toc-label='get_all_as_string' .no-code-padding}
#### Description:
Returns an array of log entries as a string.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_by_mod_as_resource(` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_by_mod_as_resource data-toc-label='get_by_mod_as_resource' .no-code-padding}
#### Description:
Returns an array of log entries as a resource for a specific mod_name.

#### Parameters:
  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with the log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as resource for the specified `#!gd2 mod_name`.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_by_mod_as_string(` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_by_mod_as_string data-toc-label='get_by_mod_as_string' .no-code-padding}
#### Description:
Returns an array of log entries as a string for a specific mod_name.

#### Parameters:
  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with the log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings for the specified `#!gd2 mod_name`.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_by_type_as_resource(` `#!gd2 type:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_by_type_as_resource data-toc-label='get_by_type_as_resource' .no-code-padding}
#### Description:
Returns an array of log entries as a resource for a specific type.

#### Parameters:
  
`#!gd2 type` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The log type associated with the log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as resource for the specified `#!gd2 type`.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_by_type_as_string(` `#!gd2 type:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_by_type_as_string data-toc-label='get_by_type_as_string' .no-code-padding}
#### Description:
Returns an array of log entries as a string for a specific type.

#### Parameters:
  
`#!gd2 type` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The log type associated with the log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings for the specified `#!gd2 type`.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_all(` `#!gd2 ) static ` {#method-get_all data-toc-label='get_all' .no-code-padding}
#### Description:
Returns an array of all log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of all log entries.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_by_mod(` `#!gd2 mod_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_by_mod data-toc-label='get_by_mod' .no-code-padding}
#### Description:
Returns an array of log entries for a specific mod_name.

#### Parameters:
  
`#!gd2 mod_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with the log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries for the specified `#!gd2 mod_name`.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_by_type(` `#!gd2 type:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_by_type data-toc-label='get_by_type' .no-code-padding}
#### Description:
Returns an array of log entries for a specific type.

#### Parameters:
  
`#!gd2 type` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The log type associated with the log entries.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries for the specified `#!gd2 type`.
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_all_entries_as_string(` `#!gd2 log_entries:`&nbsp;&nbsp;[`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)`#!gd2 ) static ` {#method-get_all_entries_as_string data-toc-label='get_all_entries_as_string' .no-code-padding}
#### Description:
Returns an array of log entries represented as strings.

#### Parameters:
  
`#!gd2 log_entries` ([`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of ModLoaderLogEntry Objects.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings.
***
