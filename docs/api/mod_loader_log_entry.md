# ModLoaderLog.ModLoaderLogEntry
**Inherits**: Resource


This Sub-Class represents a log entry in ModLoader.
<hr style="border-width: thick">
## Method Descriptions
### • [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_entry()</code> {#method-get_entry data-toc-label='get_entry'}
#### Description:
Get the log entry as a formatted string.

**Returns:**
 [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)
***
### • [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_prefix()</code> {#method-get_prefix data-toc-label='get_prefix'}
#### Description:
Get the prefix string for the log entry, including the log type and mod name.

**Returns:**
 [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)
***
### • [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html) <code class="highlight">get_md5()</code> {#method-get_md5 data-toc-label='get_md5'}
#### Description:
Generate an MD5 hash of the log entry (prefix + message).

**Returns:**
 [`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_entries()</code> {#method-get_all_entries data-toc-label='get_all_entries'}
#### Description:
Get all log entries, including the current entry and entries in the stack.

**Returns:**
 [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)
***
