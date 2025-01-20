# ModLoaderLog
**Inherits**: Object


This Class provides methods for logging, retrieving logged data, and internal methods for working with log files.
<hr style="border-width: thick">

## Constants
#### • `#!gd MOD_LOG_PATH`: `#!gd "user://logs/modloader.log"` {#constant-MOD_LOG_PATH data-toc-label='MOD_LOG_PATH'} 
#### • `#!gd ERROR`: `#!gd 0` {#constant-ERROR data-toc-label='ERROR'} 
#### • `#!gd WARNING`: `#!gd 1` {#constant-WARNING data-toc-label='WARNING'} 
#### • `#!gd INFO`: `#!gd 2` {#constant-INFO data-toc-label='INFO'} 
#### • `#!gd DEBUG`: `#!gd 3` {#constant-DEBUG data-toc-label='DEBUG'} 

<hr style="border-width: thick">

## Properties
#### • `#!gd logged_messages` {#property-logged_messages data-toc-label='logged_messages'} 
#### • `#!gd verbosity` {#property-verbosity data-toc-label='verbosity'} 
#### • `#!gd ignored_mods` {#property-ignored_mods data-toc-label='ignored_mods'} 

<hr style="border-width: thick">

## Method Descriptions
### • void <code class="highlight">fatal(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-fatal data-toc-label='fatal'}
#### Description:
Logs the error in red and a stack trace. Prefixed FATAL-ERROR.



!!! note 
	*Stops execution in the editor*


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as an error.  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
 `#!gd void`
***
### • void <code class="highlight">error(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-error data-toc-label='error'}
#### Description:
Logs the message and pushes an error. Prefixed ERROR.



!!! note 
	Always logged


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as an error.  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
 `#!gd void`
***
### • void <code class="highlight">warning(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-warning data-toc-label='warning'}
#### Description:
Logs the message and pushes a warning. Prefixed WARNING.



!!! note 
	*Note: Logged with verbosity level at or above warning (-v or --log-warning).*


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a warning.  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
 `#!gd void`
***
### • void <code class="highlight">info(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-info data-toc-label='info'}
#### Description:
Logs the message. Prefixed INFO.  


!!! note 
	*Note: Logged with verbosity level at or above info (-vv or --log-info).*


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as an information.  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
 `#!gd void`
***
### • void <code class="highlight">success(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-success data-toc-label='success'}
#### Description:
Logs the message. Prefixed SUCCESS.  


!!! note 
	*Note: Logged with verbosity level at or above info (-vv or --log-info).*


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a success.  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
 `#!gd void`
***
### • void <code class="highlight">debug(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-debug data-toc-label='debug'}
#### Description:
Logs the message. Prefixed DEBUG.  


!!! note 
	*Note: Logged with verbosity level at or above debug (-vvv or --log-debug).*


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a debug.  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.

**Returns:**
 `#!gd void`
***
### • void <code class="highlight">debug_json_print(message: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), json_printable: [Variant](https://docs.godotengine.org/en/stable/classes/class_variant.html), mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), only_once: [bool](https://docs.godotengine.org/en/stable/classes/class_bool.html))</code> static {#method-debug_json_print data-toc-label='debug_json_print'}
#### Description:
Logs the message formatted with [`#!gd JSON.print()`](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json-method-print). Prefixed DEBUG.  


!!! note 
	*Note: Logged with verbosity level at or above debug (-vvv or --log-debug).*


#### Parameters:
  
`#!gd message` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The message to be logged as a debug.  
`#!gd json_printable` (Variant): The variable to be formatted and printed using [`#!gd JSON.print()`](https://docs.godotengine.org/en/stable/classes/class_json.html#class-json-method-print).  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with this log entry.  
`#!gd only_once` ([`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)): (Optional) If true, the log entry will only be logged once, even if called multiple times. Default is false.  
**Returns:**
 `#!gd void`
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_as_resource()</code> static {#method-get_all_as_resource data-toc-label='get_all_as_resource'}
#### Description:
Returns an array of log entries as a resource.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as resource.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_as_string()</code> static {#method-get_all_as_string data-toc-label='get_all_as_string'}
#### Description:
Returns an array of log entries as a string.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_by_mod_as_resource(mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_by_mod_as_resource data-toc-label='get_by_mod_as_resource'}
#### Description:
Returns an array of log entries as a resource for a specific mod_name.

#### Parameters:
  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with the log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as resource for the specified `#!gd mod_name`.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_by_mod_as_string(mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_by_mod_as_string data-toc-label='get_by_mod_as_string'}
#### Description:
Returns an array of log entries as a string for a specific mod_name.

#### Parameters:
  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with the log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings for the specified `#!gd mod_name`.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_by_type_as_resource(type: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_by_type_as_resource data-toc-label='get_by_type_as_resource'}
#### Description:
Returns an array of log entries as a resource for a specific type.

#### Parameters:
  
`#!gd type` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The log type associated with the log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as resource for the specified `#!gd type`.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_by_type_as_string(type: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_by_type_as_string data-toc-label='get_by_type_as_string'}
#### Description:
Returns an array of log entries as a string for a specific type.

#### Parameters:
  
`#!gd type` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The log type associated with the log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings for the specified `#!gd type`.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all()</code> static {#method-get_all data-toc-label='get_all'}
#### Description:
Returns an array of all log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of all log entries.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_by_mod(mod_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_by_mod data-toc-label='get_by_mod'}
#### Description:
Returns an array of log entries for a specific mod_name.

#### Parameters:
  
`#!gd mod_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the mod or ModLoader class associated with the log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries for the specified `#!gd mod_name`.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_by_type(type: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_by_type data-toc-label='get_by_type'}
#### Description:
Returns an array of log entries for a specific type.

#### Parameters:
  
`#!gd type` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The log type associated with the log entries.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries for the specified `#!gd type`.
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_entries_as_string(log_entries: [Array](https://docs.godotengine.org/en/stable/classes/class_array.html))</code> static {#method-get_all_entries_as_string data-toc-label='get_all_entries_as_string'}
#### Description:
Returns an array of log entries represented as strings.

#### Parameters:
  
`#!gd log_entries` ([`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)): An array of ModLoaderLogEntry Objects.

**Returns:**
  
- [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): An array of log entries represented as strings.
***
