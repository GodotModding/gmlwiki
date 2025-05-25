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
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">enable_mod(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-enable_mod data-toc-label='enable_mod'}
#### Description:
Enables a mod - it will be loaded on the next game start

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to enable.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to enable the mod for. Default is the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">force_enable_mod(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-force_enable_mod data-toc-label='force_enable_mod'}
#### Description:
Forces a mod to enable, ensuring it loads at the next game start, regardless of load warnings.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to enable.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile for which the mod will be enabled. Defaults to the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">disable_mod(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-disable_mod data-toc-label='disable_mod'}
#### Description:
Disables a mod - it will not be loaded on the next game start

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to disable.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to disable the mod for. Default is the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">set_mod_current_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-set_mod_current_config data-toc-label='set_mod_current_config'}
#### Description:
Sets the current config for a mod in a user profile's mod_list.

#### Parameters:
  
- `#!gd2 mod_id` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd2 mod_config` ([`#!gd2 ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The mod config to set as the current config.  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to update. Default is the current user profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">create_profile(profile_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-create_profile data-toc-label='create_profile'}
#### Description:
Creates a new user profile with the given name, using the currently loaded mods as the mod list.

#### Parameters:
  
- `#!gd2 profile_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the new user profile (must be unique).

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">set_profile(user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-set_profile data-toc-label='set_profile'}
#### Description:
Sets the current user profile to the given user profile.

#### Parameters:
  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): The user profile to set as the current profile.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">delete_profile(user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-delete_profile data-toc-label='delete_profile'}
#### Description:
Deletes the given user profile.

#### Parameters:
  
- `#!gd2 user_profile` ([`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): The user profile to delete.

**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True on success.
***
### • [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) <code class="highlight">get_current()</code> static {#method-get_current data-toc-label='get_current'}
#### Description:
Returns the current user profile.

**Returns:**
  
- [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html): The current profile or `#!gd2 null` if not set.
***
### • [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) <code class="highlight">get_profile(profile_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_profile data-toc-label='get_profile'}
#### Description:
Returns the user profile with the given name.

#### Parameters:
  
- `#!gd2 profile_name` ([`#!gd2 String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the user profile to retrieve.

**Returns:**
  
- [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html): The profile or `#!gd2 null` if not found
***
### • [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_as_array()</code> static {#method-get_all_as_array data-toc-label='get_all_as_array'}
#### Description:
Returns an array containing all user profiles stored in ModLoaderStore.

**Returns:**
  
- [`#!gd2 Array`](https://docs.godotengine.org/en/stable/classes/class_array.html): A list of [`#!gd2 ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) Objects
***
### • [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">is_initialized()</code> static {#method-is_initialized data-toc-label='is_initialized'}
#### Description:
Returns true if the Mod User Profiles are initialized.   
**Returns:**
  
- [`#!gd2 bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if profiles are ready.   
On the first execution of the game, user profiles might not yet be created. Use this method to check if everything is ready to interact with the ModLoaderUserProfile API.
***
