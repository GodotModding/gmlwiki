---
description: This Sub-Class represents a log entry in ModLoader.
---

# ModLoaderLog.ModLoaderLogEntry
**Inherits**: Resource


This Sub-Class represents a log entry in ModLoader.
<hr style="border-width: thick">

## Properties
#### • `#!gd2 mod_name` {#property-mod_name data-toc-label='mod_name'} 
#### • `#!gd2 message` {#property-message data-toc-label='message'} 
#### • `#!gd2 type` {#property-type data-toc-label='type'} 
#### • `#!gd2 time` {#property-time data-toc-label='time'} 
#### • `#!gd2 time_stamp` {#property-time_stamp data-toc-label='time_stamp'} 
#### • `#!gd2 stack` {#property-stack data-toc-label='stack'} 

<hr style="border-width: thick">

## Method Descriptions
### • [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_entry()</code> {#method-get_entry data-toc-label='get_entry'}
#### Description:
Get the log entry as a formatted string.

**Returns:**
 [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)
***
### • [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_prefix()</code> {#method-get_prefix data-toc-label='get_prefix'}
#### Description:
Get the prefix string for the log entry, including the log type and mod name.

**Returns:**
 [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)
***
### • [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_md5()</code> {#method-get_md5 data-toc-label='get_md5'}
#### Description:
Generate an MD5 hash of the log entry (prefix + message).

**Returns:**
 [`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_entries()</code> {#method-get_all_entries data-toc-label='get_all_entries'}
#### Description:
Get all log entries, including the current entry and entries in the stack.

**Returns:**
 [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)
***
