<!-- currently this document only covers the Markdown styling, nothing to do with the content of the docs -->

# Contributing to Our Documentation
Hey there! 🎉 Thanks for thinking about contributing to the [Godot Mod Loader](https://github.com/GodotModding/godot-mod-loader) docs. Here's a quick guide to get you started.

## Getting Started
1. **Fork the Repo:** Click the "Fork" button at the top right of the repo page.
2. **Clone Your Fork:** On your machine, run:
```bash
git clone https://github.com/your-username/gmlwiki
cd gmlwiki
```
3. **Use Docsify to Locally Host the Docs:** run: `docsify serve docs/`

> [!NOTE]
> Nearly *all* documentation is done using Markdown files. It's as simple as modifing one of these files and opening a PR. To keep things organized please continue reading!


## Doc Structure
The docs are laid out in a pretty straight forward manner. Everything here assumes the "root" of the project means the `docs/` directory!

### Directories
- `_plugins/` - A folder at the root directory which stores all custom Docsify plugins
- `_media/` - A folder included wherever media (png, mp3, mp4, etc...) is used. If your media is only used inside of one directory please use a directory specific `_media/` folder.
- `api/` - A folder containing the Godot Mod Loader api documentation. As a rule of thumb do not mess with these directly, if you spot a problem make an [issue](https://github.com/GodotModding/gmlwiki/issues) or [contact us](https://discord.godotmodding.com/).
- `guides/` - A folder containing guides of some sort. With sub folders for specific types of guides E.g. integration or modding.
- `misc/` - A folder where all *other* things exist. If you find something that doesn't belong anywhere, create a folder where it does. Be sure to make this known in your PR.

### Important Files
- `index.html` - The heart and soul of the project. If you choose to tamper with this file please be sure to read [Docsify's Documentation](https://docsify.js.org/#/)!
- `style.css` - The lipstick to the project, this file modifies (and creates it's own) styling for the docs.
- `_sidebar.md` - Used by Docsify to generate the sidebar. More info on this at [_sidebar.md](#_sidebarmd).

*some worthy mentions are `_todo.md`, `_404.md`, and `_coverpage.md` but these shouldn't need to be modified*


## How to Create a New Page
Creating a new page is simple. Just create a markdown file where it seems aproprite, for an example lets say `guides/modding/epic_mod_guide.md` then add it to the sidebar (more info at [_sidebar.md](#_sidebarmd)).

> [!NOTE]
> The name of your file should be snake_case. Only in certain cases (like with `api/`) should this change.

If your page leads somewhere which isn't created yet (or is soon to be created) please link to `_todo` E.g. `[Epic and Cool Page](_todo)`

## _sidebar.md
The sidebar is a pretty core part of navigating the docs. As such it's important to know how to modify the sidebar. 

For adding sections use html syntax like so `- <span>section title</span>`
For adding sub-sections use html syntax like so `- <span class="subsection">sub-section title</span>`
For adding pages use a markdown syntax like so `- [display name](markdown_file_location.md)` E.g. `- [Hello World!](hello_world.md)`
