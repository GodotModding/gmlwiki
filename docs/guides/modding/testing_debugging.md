# Testing and Debugging Your Mods

## Quick Steam Workshop Test

Since your mods will usually be used in the exported game, not from the editor, and there are a few differences between
these two environments, you will likely want a way to quickly change something, export and run the game like your 
mod players would.

For this purpose, you can set the output path in the [Mod Tool](tools/mod_tool.md) to a subfolder of the
[steam workshop folder](file_paths.md#steam-workshop-folder). 

![bottom area of the mod tool panel, showing the export path](_media/mod_tool_workshop_export.png)

If you don't have a steam workshop ID yet, you can just place a new folder with any name in its place, 
for example `.../workshop/content/<game steam id>/quicktest`

On export, this will place your new mod zip right where the game expects it, and you can test your mod in the steam game.

## Logging and other handy options

If you are missing information about why your mod is not loading correctly or at all, you can enable more logging 
information in the output console at the bottom by searching for `options.tres` in the file system dock.(1) 
Double-clicking this file will open the [Mod Loader Options](../integration/mod_loader_options.md) in the inspector(2). 
There are multiple options - the "current" or default resource at the top and some feature overrides - there is 
usually an editor-specific override, which you will want to fold out by clicking on the box. 
{ .annotate }

1.  Located in the bottom left corner by default
2.  Located on the right side by default


![options resource as seen in the inspector](_media/options_resource_inspector.png) 
{ .half-width .center }

These options can set a few useful options, like the log level - setting this to DEBUG will allow you to see much more 
information about the loading process. 

If you are upgrading a mod to a newer version, we also recommend you to disable
ignoring deprecation errors - these errors will tell you where you need to fix your mod so that it doesn't break for the 
next GML version.



