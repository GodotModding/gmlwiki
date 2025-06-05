Hey there! 🎉 Thanks for thinking about contributing to the [Godot Mod Loader](https://github.com/GodotModding/godot-mod-loader) documentation. 

Most of this documentation uses basic [Markdown](https://www.markdownguide.org/basic-syntax/). 
Updating the documentation is as simple as modifying one of the files and opening a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). You can also just send us the file on our [Discord](https://discord.godotmodding.com/).

If you want to go more in-depth and preview your changes better, *here's a quick guide* to get you started.

## 🔧 Setup
1. Install [Python](https://docs.python.org/3/using/index.html) on your system.
2. Fork and clone this repository: [GitHub Tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
3. **(Optional, but recommended)** Create and activate a virtual environment:
   ```shell
   python -m venv .
   source bin/activate  # On Windows use: .\Scripts\activate
   ```
4. Install requirements:
   ```shell
    pip install -r requirements.txt
    ```
5. Start MkDocs: 
    ```shell
    mkdocs serve
    ```
6. Open the local docs in your browser: http://127.0.0.1:8000/

To keep things organized, please continue reading!

## 📁 Docs Structure
All documentation needs to be in the `docs/` directory; files outside of it are ignored.

### Subdirectories
#### `api/`
Auto-generated API reference. Found an issue? [Open an issue](https://github.com/GodotModding/gmlwiki/issues) or [message us](https://discord.godotmodding.com/).

#### `guides/`
Guides for modders and game developers. Subfolders separate the two.

#### `misc/`
This folder contains pages that don't fit the first category. If you find something that doesn't belong anywhere, create a folder where it does. Be sure to make this known in your PR!

#### `_media/`
Media files (PNG, MP3, etc.). Place them in a local `_media/` subfolder if they are only used in one folder.

## 📝 Adding New Pages
Make sure the name of your file is in snake_case!

After adding a new page, make sure to include it in the sidebar navigation by adding it to [`mkdocs.yml`](./mkdocs.yml)

## ✏️ Editing Tips
MkDocs [requires relative links](https://www.mkdocs.org/user-guide/writing-your-docs/#internal-links) that point to `.md` files.

###### BAD
```md
[Script Hooks](/guides/modding/script_hooks/)
```

###### GOOD
```md
[Script Hooks](script_hooks.md)
```

###### To link across folders:
```md
[API Reference](../../api/mod_loader_mod.md)
```

###### To link to a header:
```
mod_loader_mod.md#method-install_script_extension
```

> [!NOTE]
> Installed extensions can be found at the end of [`mkdocs.yml`](./mkdocs.yml)

Useful extended markdown features:
* [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) for notes, warnings, etc.
* [Tooltips](https://squidfunk.github.io/mkdocs-material/reference/tooltips/#usage) and abbreviations in [abbreviations.md](includes/abbreviations.md) 
* [Code Blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/) 
* [Content Tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/) 

# Godot Code Tabs / Blocks
> [!NOTE]
> We use `gdscript2` and `gd2` instead of `gdscript` and `gd` because we've replaced the [default gdscript lexer](https://github.com/pygments/pygments/blob/master/pygments/lexers/gdscript.py)
> with [our own](https://github.com/GodotModding/pygments-gdscript), adding a new alias to lex is cleaner than hacking the Pygments plugin system to replace the old lexer.

Here's a reusable snippet:
```markdown
=== "Godot 4"

    ```gdscript2
    [...]
    ```

=== "Godot 3"

    ```gdscript2
    [...]
    ```
```

Code blocks can also highlight single or a range of lines by adding this   
`gdscript2 hl_lines="1 2-5"`

For [inline code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#highlighting-inline-code-blocks) use `#!gd2 print("hello world")`

As a general rule of thumb, use `gd2` for inline brevity, and `gdscript2` for block clarity.

## 🔄 API Doc Generation

1. Replace `godot4.3` with your Godot editor path or alias.
2. From the project directory, run:
```shell
git submodule init
git submodule sync
git submodule update --remote
cd godot-mod-loader
godot4.3 --doctool ../gdscript_docs --gdscript-docs res://addons/mod_loader/api/ --quit
cd ..
python3 xml_to_md.py
```

The path set with `--gdscript-docs` needs to start with `res://`, otherwise godot can't find the files.   
[workaround credit](https://github.com/godotengine/godot/issues/84579#issuecomment-1873346477)

Docs must be generated from the project root. As such, we `cd` into the submodule and out when we're done, otherwise you'll get parse errors.

## Syntax Highlights
We match MkDocs highlighting colors to the Godot editor theme.

> [!NOTE]
> Due to an outdated default GDScript lexer, we use our [own lexer](https://github.com/GodotModding/pygments-gdscript) with the `gdscript2`/`gd2` aliases.

We used this small script to get the colors from the current editor theme and match
them to the CSS variables or classes used by mkdocs material.

MkDocs Material classes: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/?h=highlight#customization
Fine-grained classes: https://github.com/squidfunk/mkdocs-material/blob/master/src/templates/assets/stylesheets/main/extensions/pymdownx/_highlight.scss
Pygments tokens available by default: https://pygments.org/docs/tokens/

```gdscript
@tool
extends Node

@export var run_now := false:
	set(val):
		run()


func run():
	var prefix := "text_editor/theme/highlighting/"
	var colors := {
		"symbol_color": ["--md-code-hl-operator-color", "--md-code-hl-punctuation-color"],
		"keyword_color": ["--md-code-hl-keyword-color", "--md-code-hl-special-color", ".bp"],
		"control_flow_keyword_color": [".k.k-ControlFlow"],
		"base_type_color": [".nb.nb-Type"],
		"engine_type_color": [".nb"],
		"user_type_color": [".nc"],
		"comment_color": ["--md-code-hl-comment-color"],
		"doc_comment_color": [".c.c-Doc"],
		"string_color": ["--md-code-hl-string-color"],
		"background_color": ["--md-code-bg-color"],
		"completion_background_color": [""],
		"completion_selected_color": [""],
		"completion_existing_color": [""],
		"completion_font_color": [""],
		"text_color": ["--md-code-hl-generic-color", "--md-code-hl-name-color", "--md-code-fg-color"],
		"line_number_color": [""],
		"safe_line_number_color": [""],
		"caret_color": [""],
		"selection_color": [""],
		"brace_mismatch_color": [""],
		"current_line_color": [""],
		"line_length_guideline_color": [""],
		"word_highlighted_color": ["--md-code-hl-color"],
		"number_color": ["--md-code-hl-number-color"],
		"function_color": ["--md-code-hl-function-color"],
		"member_variable_color": ["--md-code-hl-variable-color", "--md-code-hl-constant-color", ".vi"],
		"mark_color": [""],
		"breakpoint_color": [""],
		"code_folding_color": [""],
		"folded_code_region_color": [".c.c-Region"],
		"search_result_color": [""],

		"gdscript/function_definition_color": [""],
		"gdscript/global_function_color": [".nb.nb-Function"],
		"gdscript/node_path_color": [".s.s-NodePath"],
		"gdscript/node_reference_color": [".sx"],
		"gdscript/annotation_color": [".nd"],
		"gdscript/string_name_color": [".s.s-StringName"],
	}


	var settings := EditorInterface.get_editor_settings()

	var color_classes := ""
	print("{")
	print("\t--godot-theme-base-color: #%s;\n" % settings.get("interface/theme/base_color").to_html(true))
	for color_name in colors:
		var color: Color = settings.get(prefix + color_name)
		#print('\t"%s": "#%s",  # %s' % [color_name, color.to_html(false), ", ".join(colors[color_name])])
		for css_thing: String in colors[color_name]:
			if css_thing.begins_with("--"):
				print("\t%s: #%s;" % [css_thing, color.to_html(true)])
			elif css_thing.begins_with("."):
				var css_var := "--md-code-hl-custom-class%s" % css_thing.replace(".", "_")
				print("\t%s: #%s;" % [css_var, color.to_html(true)])
				color_classes += "\n.highlight %s {\n\tcolor: var(%s);\n}\n" % [css_thing, css_var]
	print("}")
	print(color_classes)
```
