# ModLoaderUserProfile
**Inherits**: Object


This Class provides methods for working with user profiles.
<hr style="border-width: thick">
## Constants
- `#!gd LOG_NAME`: `#!gd "ModLoader:UserProfile"`
- `#!gd FILE_PATH_USER_PROFILES`: `#!gd "user://mod_user_profiles.json"`
<hr style="border-width: thick">
## Method Descriptions
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">enable_mod(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-enable_mod data-toc-label='enable_mod'}
#### Description:
Enables a mod - it will be loaded on the next game start  
  
#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to enable.  
- `#!gd user_profile` ([`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to enable the mod for. Default is the current user profile.  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">force_enable_mod(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-force_enable_mod data-toc-label='force_enable_mod'}
#### Description:
Forces a mod to enable, ensuring it loads at the next game start, regardless of load warnings.  
  
#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to enable.  
- `#!gd user_profile` ([`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile for which the mod will be enabled. Defaults to the current user profile.  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html): True if the mod is successfully set to enable, False otherwise.
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">disable_mod(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-disable_mod data-toc-label='disable_mod'}
#### Description:
Disables a mod - it will not be loaded on the next game start  
  
#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod to disable.  
- `#!gd user_profile` ([`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to disable the mod for. Default is the current user profile.  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">set_mod_current_config(mod_id: [String](https://docs.godotengine.org/en/stable/classes/class_string.html), mod_config: [ModConfig](https://docs.godotengine.org/en/stable/classes/class_modconfig.html), user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-set_mod_current_config data-toc-label='set_mod_current_config'}
#### Description:
Sets the current config for a mod in a user profile's mod_list.  
  
#### Parameters:
  
- `#!gd mod_id` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The ID of the mod.  
- `#!gd mod_config` ([`#!gd ModConfig`](https://docs.godotengine.org/en/stable/classes/class_modconfig.html)): The mod config to set as the current config.  
- `#!gd user_profile` ([`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): (Optional) The user profile to update. Default is the current user profile.  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">create_profile(profile_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-create_profile data-toc-label='create_profile'}
#### Description:
Creates a new user profile with the given name, using the currently loaded mods as the mod list.  
  
#### Parameters:
  
- `#!gd profile_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the new user profile (must be unique).  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">set_profile(user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-set_profile data-toc-label='set_profile'}
#### Description:
Sets the current user profile to the given user profile.  
  
#### Parameters:
  
- `#!gd user_profile` ([`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): The user profile to set as the current profile.  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)
***
### • [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html) <code class="highlight">delete_profile(user_profile: [ModUserProfile](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html))</code> static {#method-delete_profile data-toc-label='delete_profile'}
#### Description:
Deletes the given user profile.  
  
#### Parameters:
  
- `#!gd user_profile` ([`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)): The user profile to delete.  
  
**Returns:**
 [`#!gd bool`](https://docs.godotengine.org/en/stable/classes/class_bool.html)
***
### • [`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) <code class="highlight">get_current()</code> static {#method-get_current data-toc-label='get_current'}
#### Description:
Returns the current user profile.  
  
**Returns:**
 [`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html)
***
### • [`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) <code class="highlight">get_profile(profile_name: [String](https://docs.godotengine.org/en/stable/classes/class_string.html))</code> static {#method-get_profile data-toc-label='get_profile'}
#### Description:
Returns the user profile with the given name.  
  
#### Parameters:
  
- `#!gd profile_name` ([`#!gd String`](https://docs.godotengine.org/en/stable/classes/class_string.html)): The name of the user profile to retrieve.  
  
**Returns:**
 [`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) or `#!gd null` if not found
***
### • [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) <code class="highlight">get_all_as_array()</code> static {#method-get_all_as_array data-toc-label='get_all_as_array'}
#### Description:
Returns an array containing all user profiles stored in ModLoaderStore.  
  
**Returns:**
 [`#!gd Array`](https://docs.godotengine.org/en/stable/classes/class_array.html) of [`#!gd ModUserProfile`](https://docs.godotengine.org/en/stable/classes/class_moduserprofile.html) Objects
***
