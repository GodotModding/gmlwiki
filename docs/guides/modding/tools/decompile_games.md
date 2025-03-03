# Decompiling Games

!!! danger "Please be respectful to game developers." 
    Do not share any of the game's assets or source code, unless you have explicit permission from the developer. 
    
    The mod loader is made in a way that should never require your mod to contain any of the vanilla files.
    If your mod is in version control and in a public git repository, make sure it only contains your own files and use 
    a properly configured `.gitignore`.

Decompiling the game allows us to have a complete and working version, where we can see every line of code, every scene 
and every resource. Without this, modding would have to be done blindly, and we'd have to guess which functions exist - 
pretty much impossible. 

Godot games can easily be decompiled using [Godot RE Tools](https://github.com/GDRETools/gdsdecomp).  
We recommend downloading the [latest release](https://github.com/GDRETools/gdsdecomp/releases/latest), as it is 
frequently updated. Recent versions have greatly improved user experience and speed, big thanks to @nikitalita for 
maintaining the project! 

You can find the full version overview on [their GitHub releases page](https://github.com/GDRETools/gdsdecomp/releases). 

Decompiling with GDRE is simple: 

1. Find the [game files](../file_paths.md#game-files). You specifically need the `<GAME NAME>.pck` file 
    - if the `.pck` is not in this folder, proceed with the `.exe` or `.app` - they contain the pck. 
2. Open the game file in GDRE, there are multiple ways to do this
    - The simple: drag and drop the file into the GDRE window
    - The traditional: in the application, select `RE Tools` in the top menu bar -> `Recover Project...` -> then navigate to, and select the game file
    - The permanent: right-click the `.pck` in your file explorer -> open with -> select GDRE (enable always use this option if you decomp frequently)
3. Once opened, wait until decompiled, then choose a location to save the recovered files to
    ![gdre extract window, showing an overview of the extracted files and choosing the output location in the bottom right](_media/gdre_extract_location.png)
    Make sure the default "Full recovery" option wasn't accidentally changed and that no folder was unchecked in the list.
4. Have a quick read through the export log, it will tell you which version
    of Godot was used to create the project. You need to use the exact same version to avoid crashes. 
5. Extraction done! Start Godot and [open the game](https://docs.godotengine.org/en/stable/tutorials/editor/project_manager.html#opening-and-importing-projects)
