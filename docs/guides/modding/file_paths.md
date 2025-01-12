# Godot User Files

## Common Files in the User Folder
**Logs** are all stored in the `/logs` folder.  
The most recent one does not have a time stamp (named `godot.log` or `godot` if the extension is hidden)

Deleting settings and save files can resolve some issues, but can of course reset stuff. It's safer to move them to another folder as backup. File names differ for each game, fill them in for your community if you know them.  
**Saves** are named `###`  
**Settings** are named `###`  

`Note:` If the files do not appear here for a Steam game, disable Steam cloud saves and make sure you are in online mode. They will appear shortly after.
Right-click the game in your library sidebar -> Properties -> General -> disable Steam Cloud

## Folder Locations
Make sure to actually replace `<GAME NAME>` with the name of the game you are looking for. Or leave it out and navigate the last step by hand if you don't know the exact folder name.

### Godot App Userdata
#### Windows: 
press ++win+r++, search 
```
%appdata%/godot/app_userdata/<GAME NAME>
```
or manually navigate to
```
C:\Users\<YOUR USERNAME>\AppData\Roaming\Godot\app_userdata\<GAME NAME>
```
#### Linux: 
navigate to
```
~/.local/share/godot/app_userdata/<GAME NAME>
```
#### Mac: 
open Finder, press ++cmd+shift+g++, search
```
~/Library/Application Support/Godot/app_userdata/<GAME NAME>
```
or manually navigate to
```
/Users/<YOUR USERNAME>/Library/Application Support/Godot/app_userdata/<GAME NAME>
```
note that `Library` is a hidden folder, press ++cmd+shift+period++ to toggle hidden folder visibility in Finder

### Steam workshop files

1. In Steam, right-click the game in the left sidebar -> "Manage" -> "Browse local files".  
2. This will take you to `[...]/steamapps/common/<GAME NAME>`
3. Navigate two folders back, to `/steamapps`. This folder also contains `/workshop`
4. Navigate to `[...]/steamapps/workshop/content/<STEAM GAME ID>/<WORKSHOP ITEM ID>`

Note:
The two Steam IDs can be found in their store and workshop links   
Game store page: `https://store.steampowered.com/app/1637320/Dome_Keeper/` -> `1637320`  
Workshop item page: `https://steamcommunity.com/sharedfiles/filedetails/?id=2440099853` -> `2440099853`

