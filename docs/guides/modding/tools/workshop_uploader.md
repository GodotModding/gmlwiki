---
description: How to upload your mod to the Steam Workshop
---

# Steam Workshop Uploader

[//]: # (TODO)
!!! example "Documentation in progress"

## Usage

Usually, uploading is done through the [godot-workshop-utility](https://github.com/Blobfish-Games/godot-workshop-utility/).
From game to game this workshop utility may look slightly different, depending on how the developer implemented it. 
You may find the uploader on a separate Steam beta branch, as a startup option, or as a scene to run individually in 
the decompiled source code - which option was chosen should be somewhere in your game's specific documentation. 

The interface has at least one required and two optional input fields:

1. The required one wants the file path to your mod file, this is the bundle of zipped files you have created 
when you [exported your mod](../distributing_mods.md#exporting).  
2. The first optional input wants the file path to a preview image, this is the icon that will be visible in the Steam 
Workshop. More about it in a second.
3. The second optional input is for the Steam Workshop item ID. If this is your first upload, you can leave it empty
and Steam will generate a new ID. If you want to _update_ one of your existing items, enter the item's ID - if you
forgot to keep note of it, you can still find it at the end of the url on the [workshop item page](../file_paths.md#workshop-folder). 

[//]: # (steam tags?)

The icon size should not exceed 1MB, otherwise the workshop item upload will be rejected.  
We've found a 512 * 512px PNG works best as icon.

The Steamworks documentation also notes:
> The format should be one that both the web and the application (if necessary) can render. Suggested formats include JPG, PNG and GIF.
> Be sure your app has its Steam Cloud quota and number of files set, as preview images are stored under the user's Cloud. If your app has no Cloud values set, this call will fail.

While GIFs work on Steam, Godot applications can't easily render them, so if there is an in-game preview it may break.  
The cloud quota is something the developer sets, this is usually set pretty high and should not be an issue though.

## Troubleshooting

!!! bug "Common Issue"
    Steam needs to be running and your session needs to be online while you use this tool.
    
    You also need the [GodotSteam](godot_steam.md) version of Godot.

The most common issue is error 25, which is usually caused by the icon being wrong in some way. 
If you have this issue and have followed the notes above, you can try the upload without an icon. Ugly, but usually works.

There may also be a possible workaround for the icon upload using SteamCMD, as described here: 
[https://steamcommunity.com/sharedfiles/filedetails/?id=2936720761](https://steamcommunity.com/sharedfiles/filedetails/?id=2936720761) (or: [Archived](https://web.archive.org/web/20250108143743/https://steamcommunity.com/sharedfiles/filedetails/?id=2936720761))

If the upload fails, Steam returns an error code. These error codes have a specific message which may help. 

| Code | Name                    | Message                                                                                                                                                                                                        |
|------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `1`  | `OK`                    | The operation completed successfully.                                                                                                                                                                          |
| `8`  | `InvalidParam`          | One of the submission fields contains something not being accepted by that field.                                                                                                                              |
| `9`  | `FileNotFound`          | The uploaded file could not be found.                                                                                                                                                                          |
| `14` | `DuplicateName`         | The user already has a Steam Workshop item with that name.                                                                                                                                                     |
| `15` | `AccessDenied`          | There was a problem trying to save the title and description. Access was denied.                                                                                                                               |
| `16` | `Timeout`               | The operation took longer than expected. Have the user retry the creation process.                                                                                                                             |
| `17` | `Banned`                | The user doesn't have permission to upload content to this hub because they have an active VAC or Game ban.                                                                                                    |
| `20` | `ServiceUnavailable`    | The workshop server hosting the content is having issues - have the user retry.                                                                                                                                |
| `21` | `NotLoggedOn`           | The user is not currently logged into Steam.                                                                                                                                                                   |
| `24` | `InsufficientPrivilege` | The user is currently restricted from uploading content due to a hub ban, account lock, or community ban. They would need to contact Steam Support.                                                            |
| `25` | `LimitExceeded`         | The user has exceeded their Steam Cloud quota. Have them remove some items and try again.                                                                                                                      |
| `29` | `DuplicateRequest`      | The file was already successfully uploaded. The user just needs to refresh.                                                                                                                                    |
| `44` | `ServiceReadOnly`       | Due to a recent password or email change, the user is not allowed to upload new content. Usually this restriction will expire in 5 days, but can last up to 30 days if the account has been inactive recently. |

Reference:

- [Error codes for the upload](https://partner.steamgames.com/doc/api/ISteamUGC#CreateItemResult_t)
- [All Steamworks error codes](https://partner.steamgames.com/doc/api/steam_api#EResult)
- [Setting a Workshop item icon](https://partner.steamgames.com/doc/api/ISteamUGC#SetItemPreview)
