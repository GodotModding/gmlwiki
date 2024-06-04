<!-- TODO: make this guide just as complete as the Brotato Modding Guide -->

# Decompiling Games
Use [GDRETools](https://github.com/bruvzg/gdsdecomp) to decompile a game. This will give you the full project file.
1. Open GDRETools
2. Click RE Tools > Recover Project
3. Specify the PCK location, then the export location.

?> If your PCK is embedded in the EXE, you can use GodotPCKExplorer to extract it first, but GDRE is able to handle that for a full decompilation as well.

To edit the project in Godot, you'll need to use the same Godot version the game was originally built in. GDRETools will tell you the version after decompiling.

Now, to get started, launch the Godot editor and import the project!

!> Do not share any of the game's assets or source code, unless you have explicit permission from the developer to do so. This includes creating a public repo containing the code/assets. Please be respectful to developers.