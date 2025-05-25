
This class provides methods for working with user profiles.

## Methods Overview
| Method                                              | Description                                                                                      |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [`enable_mod`](#enable_mod)                         | Enables a mod - it will be loaded on the next game start.                                        |
| [`disable_mod`](#disable_mod)                       | Disables a mod - it will not be loaded on the next game start.                                   |
| [`set_mod_current_config`](#set_mod_current_config) | Sets the current config for a mod in a user profile's mod_list.                                  |
| [`create_profile`](#create_profile)                 | Creates a new user profile with the given name, using the currently loaded mods as the mod list. |
| [`set_profile`](#set_profile)                       | Sets the current user profile to the given user profile.                                         |
| [`delete_profile`](#delete_profile)                 | Deletes the given user profile.                                                                  |
| [`get_current`](#get_current)                       | Returns the current user profile.                                                                |
| [`get_profile`](#get_profile)                       | Returns the user profile with the given name.                                                    |
| [`get_all_as_array`](#get_all_as_array)             | Returns an array containing all user profiles stored in ModLoaderStore.                          |

## Methods
### enable_mod
```gdscript2
func enable_mod(mod_id: String, user_profile: ModUserProfile) -> bool
```
Enables a mod - it will be loaded on the next game start

Parameters:
- mod_id (String): The ID of the mod to enable.
- user_profile (ModUserProfile): (Optional) The user profile to enable the mod for. Default is the current user profile.


### disable_mod
```gdscript2
func disable_mod(mod_id: String, user_profile: ModUserProfile) -> bool
```
Disables a mod - it will not be loaded on the next game start

Parameters:
- mod_id (String): The ID of the mod to disable.
- user_profile (ModUserProfile): (Optional) The user profile to disable the mod for. Default is the current user profile.


### set_mod_current_config
```gdscript2
func set_mod_current_config(mod_id: String, mod_config: ModConfig, user_profile: ModUserProfile) -> bool
```
Sets the current config for a mod in a user profile's mod_list.

Parameters:
- mod_id (String): The ID of the mod.
- mod_config (ModConfig): The mod config to set as the current config.
- user_profile (ModUserProfile): (Optional) The user profile to update. Default is the current user profile.


### create_profile
```gdscript2
func create_profile(profile_name: String) -> bool
```
Creates a new user profile with the given name, using the currently loaded mods as the mod list.

Parameters:
- profile_name (String): The name of the new user profile (must be unique).


### set_profile
```gdscript2
func set_profile(user_profile: ModUserProfile) -> bool
```
Sets the current user profile to the given user profile.

Parameters:
- user_profile (ModUserProfile): The user profile to set as the current profile.


### delete_profile
```gdscript2
func delete_profile(user_profile: ModUserProfile) -> bool
```
Deletes the given user profile.

Parameters:
- user_profile (ModUserProfile): The user profile to delete.


### get_current
```gdscript2
func get_current() -> ModUserProfile
```
Returns the current user profile.


### get_profile
```gdscript2
func get_profile(profile_name: String) -> ModUserProfile
```
Returns the user profile with the given name, or null if not found.

Parameters:
- profile_name (String): The name of the user profile to retrieve.


### get_all_as_array
```gdscript2
func get_all_as_array() -> Array
```
Returns an array containing all user profiles stored in ModLoaderStore.