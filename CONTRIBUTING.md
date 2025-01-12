# Contributing to Our Documentation
Hey there! 🎉 Thanks for thinking about contributing to the [Godot Mod Loader](https://github.com/GodotModding/godot-mod-loader) documentation. 

Most of this documentation is written using basic [Markdown](https://www.markdownguide.org/basic-syntax/). 
Updating the documentation is as simple as modifying one of the files and opening a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) - 
or even just sending us the file on our [Discord](https://discord.godotmodding.com/).

If you want to go more in-depth and preview your changes better, here's a quick guide to get you started.

## Setup

1. Install [Python](https://docs.python.org/3/using/index.html) on your system.
2. Fork and clone this repository: [GitHub Tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
3. Install requirements: 
   ```shell
    pip install -r requirements.txt
    ```
4. Start MkDocs: 
    ```shell
    mkdocs serve
    ```
5. Open the local docs in your browser: http://127.0.0.1:8000/

To keep things organized please continue reading!

## Doc Structure
All documentation needs to be in the `docs/` directory, files outside of it are ignored.

### Subdirectories
- `api/` - Contains the Godot Mod Loader api documentation. Automatically generated - if you spot any problems please open an [issue](https://github.com/GodotModding/gmlwiki/issues) or [contact us](https://discord.godotmodding.com/).
- `guides/` - Contains guides to use specific mod loader features. The sub folders logically separate guides for modders and for game developers aiming to integrate the mod loader.
- `misc/` - Contains pages that don't fit the first categories. If you find something that doesn't belong anywhere, create a folder where it does. Be sure to make this known in your PR.
- `_media/` - A folder included wherever media (png, mp3, mp4, etc...) is used. If your media is only used inside one directory please use a directory specific `_media/` folder.

## New Pages
Make sure the name of your file is in snake_case.

After adding a new page, make sure to include it in the sidebar navigation by adding it to [`mkdocs.yml`](./mkdocs.yml)

## Editing Tips

MkDocs [requires links to other doc pages](https://www.mkdocs.org/user-guide/writing-your-docs/#internal-links) 
to always be relative and to link to a `.md` file. If you use the link from the browser's 
url bar - `[Script Hooks](/guides/modding/script_hooks/)`, you will get an error:
```
Doc file 'guides/modding/script_extensions.md' contains an absolute link '/guides/modding/script_hooks/', it was left as is. Did you mean 'script_hooks.md'?
```
The correct way to link here is: `[Script Hooks](script_hooks.md)`.   
Since those are relative file paths, linking to another folder looks like this `[API Reference](../../api/ModLoaderMod.md)`   
Linking to headers is possible too by adding the part after `#` from the browser url at the end `ModLoaderMod.md#install_script_extension`

The documentation uses [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/)
which allows us to use extended Markdown. Installed extensions can be found at the end of [`mkdocs.yml`](./mkdocs.yml)

Here are a few commonly used features from the extended markdown:

To create special notes or warnings, use [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/).

To add information on hover, use [Tooltips](https://squidfunk.github.io/mkdocs-material/reference/tooltips/#usage).

[Code Blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/) and 
[Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/) 
together allow us to have highlighted code examples for Godot 3 and 4 with an easy toggle. 
The tab names need to be consistent across all pages to enable tab state synchronisation.

You can simply copy this snippet for that purpose.
```markdown
=== "Godot 4"

    ```gdscript
    [...]
    ```

=== "Godot 3"

    ```gdscript
    [...]
    ```
```

Code blocks can also highlight single or a range of lines by adding this   
`gdscript hl_lines="1 2-5"`

For codeblocks to use proper highlighting, always add the language at the top, usually `gdscript`, as seen above.

Inline code [can also be highlighted](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#highlighting-inline-code-blocks)
by adding `#!` followed by the language - `#!gd print("hello world")`

While both `gdscript` and `gd` work, the former is preferred for code blocks to be explicit while the latter
is preferred for inline highlights to remain brief.

## API Docs generation

```shell
godot4.3 --doctool docs --gdscript-docs res://addons/mod_loader/api --quit
```
The path set with `--gdscript-docs` needs to start with `res://`, otherwise godot can't find the files.   
[workaround credit](https://github.com/godotengine/godot/issues/84579#issuecomment-1873346477)