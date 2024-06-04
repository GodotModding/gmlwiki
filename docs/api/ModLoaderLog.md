<!-- top of file anchor -->
<a name=top></a>

# ModLoaderLog
This class provides methods for logging, retrieving logged data, and internal methods for working with log files.

## Methods Overview
### Logging
| Method                                  | Description                                                                                        |
|-----------------------------------------|----------------------------------------------------------------------------------------------------|
| [`fatal`](#fatal)                       | Logs the error in red and a stack trace. Prefixed FATAL-ERROR. Note: Stops the execution in editor |
| [`error`](#error)                       | Logs the message and pushes an error. Prefixed ERROR.                                              |
| [`warning`](#warning)                   | Logs the message and pushes a warning. Prefixed WARNING.                                           |
| [`info`](#info)                         | Logs the message. Prefixed INFO. **Most mods will use this.**                                      |
| [`success`](#success)                   | Logs the message. Prefixed SUCCESS.                                                                |
| [`debug`](#debug)                       | Logs the message. Prefixed DEBUG.                                                                  |
| [`debug_json_print`](#debug_json_print) | Logs the message formatted with [method JSON.print]. Prefixed DEBUG.                               |


### Accessing Stored Logs Data
| Method                                                    | Description                                                            |
|-----------------------------------------------------------|------------------------------------------------------------------------|
| [`get_all_as_resource`](#get_all_as_resource)             | Returns an array of log entries as a resource.                         |
| [`get_all_as_string`](#get_all_as_string)                 | Returns an array of log entries as a resource.                         |
| [`get_by_mod_as_resource`](#get_by_mod_as_resource)       | Returns an array of log entries as a resource for a specific mod_name. |
| [`get_by_mod_as_string`](#get_by_mod_as_string)           | Returns an array of log entries as a string for a specific mod_name.   |
| [`get_by_type_as_resource`](#get_by_type_as_resource)     | Returns an array of log entries as a resource for a specific type.     |
| [`get_by_type_as_string`](#get_by_type_as_string)         | Returns an array of log entries as a string for a specific type.       |
| [`get_all`](#get_all)                                     | Returns an array of all log entries.                                   |
| [`get_by_mod`](#get_by_mod)                               | Returns an array of log entries for a specific mod_name.               |
| [`get_by_type`](#get_by_type)                             | Returns an array of log entries for a specific type.                   |
| [`get_all_entries_as_string`](#get_all_entries_as_string) | Returns an array of log entries represented as strings.                |


## Methods
### fatal
```gdscript
func fatal(message: String, mod_name: String, only_once: bool = false) -> void
```
Logs the error in red and a stack trace. Prefixed FATAL-ERROR.

?> Stops the execution in editor

Parameters:
- message (String): The message to be logged as an error.
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### error
```gdscript
func error(message: String, mod_name: String, only_once: bool = false) -> void
```
Logs the message and pushes an error. Prefixed ERROR.

?> Always logged

Parameters:
- message (String): The message to be logged as an error.
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### warning
```gdscript
func warning(message: String, mod_name: String, only_once: bool = false) -> void
```
Logs the message and pushes a warning. Prefixed WARNING.

?> Logged with verbosity level at or above warning ([-v](/reference/cli_args)).

Parameters:
- message (String): The message to be logged as a warning.
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### info
```gdscript
func info(message: String, mod_name: String, only_once: bool = false) -> void
```
Logs the message. Prefixed INFO.

?> Logged with verbosity level at or above info ([-vv](/reference/cli_args)).

Parameters:
- message (String): The message to be logged as an information.
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### success 
```gdscript
func success(message: String, mod_name: String, only_once: bool = false) -> void
```
Logs the message. Prefixed SUCCESS.

?> Logged with verbosity level at or above info ([-vv](/reference/cli_args)).

Parameters:
- message (String): The message to be logged as a success.
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### debug
```gdscript
func debug(message: String, mod_name: String, only_once: bool = false) -> void
```
Logs the message. Prefixed DEBUG.

?> Logged with verbosity level at or above debug ([-vvv](/reference/cli_args)).

Parameters:
- message (String): The message to be logged as a debug.
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### debug_json_print
```gdscript
func debug_json_print(message: String, json_printable, mod_name: String, only_once: bool = false) -> void
```
Logs the message formatted with [method JSON.print]. Prefixed DEBUG.

?> Logged with verbosity level at or above debug ([-vvv](/reference/cli_args)).

Parameters:
- message (String): The message to be logged as a debug.
- json_printable (Variant): The variable to be formatted and printed using [method JSON.print].
- mod_name (String): The name of the mod or ModLoader class associated with this log entry.
- only_once (bool): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.


### get_all_as_resource
```gdscript
func get_all_as_resource() -> Array
```
Returns an array of log entries as a resource.

Returns:
- Array: An array of log entries represented as resource.


### get_all_as_string
```gdscript
func get_all_as_string() -> Array
```
Returns an array of log entries as a string.

Returns:
- Array: An array of log entries represented as strings.


### get_by_mod_as_resource
```gdscript
func get_by_mod_as_resource(mod_name: String) -> Array
```
Returns an array of log entries as a resource for a specific mod_name.

Parameters:
- mod_name (String): The name of the mod or ModLoader class associated with the log entries.

Returns:
- Array: An array of log entries represented as resource for the specified mod_name.


### get_by_mod_as_string
```gdscript
func get_by_mod_as_string(mod_name: String) -> Array
```
Returns an array of log entries as a string for a specific mod_name.

Parameters:
- mod_name (String): The name of the mod or ModLoader class associated with the log entries.

Returns:
- Array: An array of log entries represented as strings for the specified mod_name.


### get_by_type_as_resource
```gdscript
func get_by_type_as_resource(type: String) -> Array
```
Returns an array of log entries as a resource for a specific type.

Parameters:
- type (String): The log type associated with the log entries.

Returns:
- Array: An array of log entries represented as resource for the specified type.


### get_by_type_as_string
```gdscript
func get_by_type_as_string(type: String) -> Array
```
Returns an array of log entries as a string for a specific type.

Parameters:
- type (String): The log type associated with the log entries.

Returns:
- Array: An array of log entries represented as strings for the specified type.


### get_all
```gdscript
func get_all() -> Array
```
Returns an array of all log entries.

Returns:
- Array: An array of all log entries.


### get_by_mod
```gdscript
func get_by_mod(mod_name: String) -> Array
```
Returns an array of log entries for a specific mod_name.

Parameters:
- mod_name (String): The name of the mod or ModLoader class associated with the log entries.

Returns:
- Array: An array of log entries for the specified mod_name.


### get_by_type
```gdscript
func get_by_type(type: String) -> Array
```
Returns an array of log entries for a specific type.

Parameters:
- type (String): The log type associated with the log entries.

Returns:
- Array: An array of log entries for the specified type.


### get_all_entries_as_string
```gdscript
func get_all_entries_as_string(log_entries: Array) -> Array
```
Returns an array of log entries represented as strings.

Parameters:
- log_entries (Array): An array of ModLoaderLogEntry Objects.

Returns:
- Array: An array of log entries represented as strings.


## Sub-classes
### ModLoaderLogEntry
#### Properties
##### mod_name
```gdscript
var mod_name: String
```
Name of the mod or ModLoader class this entry refers to.


##### message
```gdscript
var message: String
```
The message of the log entry.


##### type
```gdscript
var type: String
```
The log type, which indicates the verbosity level of this entry.


##### time
```gdscript
var time: String
```
The readable format of the time when this log entry was created. Used for printing in the log file and output.


##### time_stamp
```gdscript
var time_stamp: int
```
The timestamp when this log entry was created. Used for comparing and sorting log entries by time.


##### stack
```gdscript
var stack: Array
```
An array of ModLoaderLogEntry objects. If the message has been logged before, it is added to the stack.


#### Methods
##### _init
```gdscript
func _init(_mod_name: String, _message: String, _type: String, _time: String) -> void
```
Initialize a ModLoaderLogEntry object with provided values.

Parameters:
- _mod_name (String): Name of the mod or ModLoader class this entry refers to.
- _message (String): The message of the log entry.
- _type (String): The log type, which indicates the verbosity level of this entry.
- _time (String): The readable format of the time when this log entry was created.


##### get_entry
```gdscript
func get_entry() -> String
```
Get the log entry as a formatted string.

Returns:
- String


##### get_prefix
```gdscript
func get_prefix() -> String
```
Get the prefix string for the log entry, including the log type and mod name.

Returns:
- String


##### get_md5
```gdscript
func get_md5() -> String
```
Generate an MD5 hash of the log entry (prefix + message).

Returns:
- String

##### get_all_entries
```gdscript
func get_all_entries() -> Array
```
Get all log entries, including the current entry and entries in the stack.

Returns:
- Array


### ModLoaderLogCompare
#### Methods
##### time
```gdscript
func time(a: ModLoaderLogEntry, b: ModLoaderLogEntry) -> bool
```
Custom sorter that orders logs by time


## Enumerations
##### VERBOSITY_LEVEL
```gdscript
const VERBOSITY_LEVEL: Dictionary = {"DEBUG":3,"ERROR":0,"INFO":2,"WARNING":1}
```


## Constants Descriptions
##### LOG_NAME
```gdscript
const LOG_NAME: String = "ModLoader:Log"
```

##### MOD_LOG_PATH
```gdscript
const MOD_LOG_PATH: String = "user://logs/modloader.log"
```
Path to the latest log file.