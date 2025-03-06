---
description: A brief overview of where to find a few important files and folders across your computer. 
---

# Important Files and Folders

A brief overview of where to find a few important files and folders across your computer. 

For mod specific files have a look at [mod files](mod_files.md) and [mod structure](mod_structure.md). 

## Steam

### Game files

1. In Steam, right-click the game in the left sidebar -> "Manage" -> "Browse local files".  
2. This will take you to `[...]/steamapps/common/<GAME NAME>`
3. Contents of this folder vary by OS
   - The important files for modding are the executable and the `<GAME NAME>.pck` file. 
     - The executable is essentially all of godot, which runs the game, and the `.pck` is the actual game. 
   - If the pck is not present on windows or linux, it is embedded into the `.exe`, it still exists, don't worry.
   - On macOS, the whole application is wrapped into an `.app` bundle (which is basically a fancy folder)
     - you can right-click the `.app` and "show package contents" from the context menu
     - The `.pck` is within that bundle: `/Contents/Resources/<GAME NAME>.pck`
     - The executable is: `/Contents/MacOS/<GAME NAME>`


### Workshop Folder

1. Start from the [game files](#game-files)
2. Navigate two folders back, to `/steamapps`. This folder also contains `/workshop`
3. Navigate to `[...]/steamapps/workshop/content/<STEAM GAME ID>/<WORKSHOP ITEM ID>`

Note:
The two Steam IDs can be found in their store and workshop links   
Game store page: `https://store.steampowered.com/app/1637320/Dome_Keeper/` -> `1637320`  
Workshop item page: `https://steamcommunity.com/sharedfiles/filedetails/?id=2440099853` -> `2440099853`



## Godot User Data Location

This refers to Godot's default user data folder, also known as `user://` in the editor.

=== "Windows" 
    press ++win+r++, search 
    ```
    %appdata%/godot/app_userdata/<GAME NAME>
    ```
    or manually navigate to
    ```
    C:\Users\<YOUR USERNAME>\AppData\Roaming\Godot\app_userdata\<GAME NAME>
    ```
=== "Linux" 
    navigate to
    ```
    ~/.local/share/godot/app_userdata/<GAME NAME>
    ```
=== "macOS" 
    open Finder, press ++cmd+shift+g++, search
    ```
    ~/Library/Application Support/Godot/app_userdata/<GAME NAME>
    ```
    or manually navigate to
    ```
    /Users/<YOUR USERNAME>/Library/Application Support/Godot/app_userdata/<GAME NAME>
    ```
    !!! tip
        `Library` is a hidden folder, press ++cmd+shift+period++ to toggle hidden folder visibility in Finder

!!! note
    Make sure to actually replace `<GAME NAME>` with the name of the game you are looking for. 
    Or leave it out and navigate the last step by hand if you don't know the exact folder name.

### Common User Data

Logs are useful for troubleshooting many issues in the running game, both for game and mod developers equally. They 
contain what you'd usually see in the console output of the editor.  
They are all stored in the `/logs` folder within `user://`.  
The most recent log does not have a time stamp (named just `godot.log` and might be shown as `godot` if the extension 
is hidden). 

It's common for settings and game saves to be in this folder too.
Deleting settings and save files can resolve some issues, but can of course reset progress. 
It's safer to move them to another folder as backup. File names differ for each game.

!!! Tip
    If the files do not appear here for a Steam game, disable Steam cloud saves and make sure you are in online mode. They will appear shortly after.
    Right-click the game in your library sidebar -> Properties -> General -> disable Steam Cloud
