---
description: This Class provides methods for working with user profiles.
---

# ModLoaderUserProfile
**Inherits**: Object


This Class provides methods for working with user profiles.
<hr style="border-width: thick">

## Constants
#### • `#!gd2 LOG_NAME`: `#!gd2 "ModLoader:UserProfile"` {#constant-LOG_NAME data-toc-label='LOG_NAME'} 
#### • `#!gd2 FILE_PATH_USER_PROFILES`: `#!gd2 "user://mod_user_profiles.json"` {#constant-FILE_PATH_USER_PROFILES data-toc-label='FILE_PATH_USER_PROFILES'} 

<hr style="border-width: thick">

## Method Descriptions
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 enable_mod(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 user_profile:`&nbsp;&nbsp;[`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)`#!gd2 ) static ` {#method-enable_mod data-toc-label='enable_mod' .no-code-padding}
#### Description:
Enables a mod - it will be loaded on the next game start

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to enable.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to enable the mod for. Default is the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 force_enable_mod(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 user_profile:`&nbsp;&nbsp;[`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)`#!gd2 ) static ` {#method-force_enable_mod data-toc-label='force_enable_mod' .no-code-padding}
#### Description:
Forces a mod to enable, ensuring it loads at the next game start, regardless of load warnings.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to enable.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile for which the mod will be enabled. Defaults to the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 disable_mod(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 user_profile:`&nbsp;&nbsp;[`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)`#!gd2 ) static ` {#method-disable_mod data-toc-label='disable_mod' .no-code-padding}
#### Description:
Disables a mod - it will not be loaded on the next game start

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to disable.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to disable the mod for. Default is the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 set_mod_current_config(` `#!gd2 mod_id:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 , ` `#!gd2 mod_config:`&nbsp;&nbsp;[`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)`#!gd2 , ` `#!gd2 user_profile:`&nbsp;&nbsp;[`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)`#!gd2 ) static ` {#method-set_mod_current_config data-toc-label='set_mod_current_config' .no-code-padding}
#### Description:
Sets the current config for a mod in a user profile's mod_list.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd2 mod_config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The mod config to set as the current config.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to update. Default is the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 create_profile(` `#!gd2 profile_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-create_profile data-toc-label='create_profile' .no-code-padding}
#### Description:
Creates a new user profile with the given name, using the currently loaded mods as the mod list.

#### Parameters:
  
- `#!gd2 profile_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the new user profile (must be unique).

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 set_profile(` `#!gd2 user_profile:`&nbsp;&nbsp;[`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)`#!gd2 ) static ` {#method-set_profile data-toc-label='set_profile' .no-code-padding}
#### Description:
Sets the current user profile to the given user profile.

#### Parameters:
  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): The user profile to set as the current profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 delete_profile(` `#!gd2 user_profile:`&nbsp;&nbsp;[`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)`#!gd2 ) static ` {#method-delete_profile data-toc-label='delete_profile' .no-code-padding}
#### Description:
Deletes the given user profile.

#### Parameters:
  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): The user profile to delete.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)&nbsp;&nbsp;`#!gd2 get_current(` `#!gd2 ) static ` {#method-get_current data-toc-label='get_current' .no-code-padding}
#### Description:
Returns the current user profile.

**Returns:**
  
- [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html): The current profile or `#!gd2 null` if not set.
***
### • [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)&nbsp;&nbsp;`#!gd2 get_profile(` `#!gd2 profile_name:`&nbsp;&nbsp;[`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)`#!gd2 ) static ` {#method-get_profile data-toc-label='get_profile' .no-code-padding}
#### Description:
Returns the user profile with the given name.

#### Parameters:
  
- `#!gd2 profile_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the user profile to retrieve.

**Returns:**
  
- [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html): The profile or `#!gd2 null` if not found
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html)&nbsp;&nbsp;`#!gd2 get_all_as_array(` `#!gd2 ) static ` {#method-get_all_as_array data-toc-label='get_all_as_array' .no-code-padding}
#### Description:
Returns an array containing all user profiles stored in ModLoaderStore.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): A list of [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) Objects
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)&nbsp;&nbsp;`#!gd2 is_initialized(` `#!gd2 ) static ` {#method-is_initialized data-toc-label='is_initialized' .no-code-padding}
#### Description:
Returns true if the Mod User Profiles are initialized.   
**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if profiles are ready.   
On the first execution of the game, user profiles might not yet be created. Use this method to check if everything is ready to interact with the ModLoaderUserProfile API.
***
