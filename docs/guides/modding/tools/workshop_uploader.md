# Steam Workshop uploader

[//]: # (TODO)
!!! example "Documentation in progress"

## Usage

if you already have a workshop item make sure to set the id (can be found in the url)

setting paths from the interface

adding an icon (aka preview image)
the steam rules seem to be
- square?
- 512x512px max
- png or jpg
- not over 1MB? 
- perhaps only a specific color format works?

## Error codes
reference: [Steamworks Documentation](https://partner.steamgames.com/doc/api/steam_api#EResult) and [https://steamerrors.com/](https://steamerrors.com/)

Most common: error 25
this is usually caused by the icon being wrong in some way. the upload usually works if no icon is added.

[//]: # (https://partner.steamgames.com/doc/api/ISteamUGC#SetItemPreview)

possible workaround using steamCMD
https://steamcommunity.com/sharedfiles/filedetails/?id=2936720761

once uploaded the item will be private by default, you can change this in the right sidebar under "visibility"

you can add additional images and description from the steam interface under "edit title and description" and "add images"
note that the title will be overwritten when you upload a new version

[//]: # (steam tags?)


