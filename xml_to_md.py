import os
import xml.etree.ElementTree as ElementTree
import re


def bbcode_to_markdown(text):
	text = text.strip()
	# Convert italic [i] to *italic*
	text = re.sub(r'\[i](.*?)\[/i]', r'*\1*', text)
	# Convert bold [b] to **bold**
	text = re.sub(r'\[b](.*?)\[/b]', r'**\1**', text)
	# Convert underlined [u] to ^^underlined^^
	text = re.sub(r'\[u](.*?)\[/u]', r'^^\1^^', text)
	# Convert strikethrough [s] to ~~strikethrough~~
	text = re.sub(r'\[s](.*?)\[/s]', r'~~\1~~', text)
	# Convert code [code] to `code`, with inline highlight
	text = re.sub(r'\[code](.*?)\[/code]', r'`#!gd \1`', text)
	# Convert codeblock [codeblock] to triple backticks for code block
	# TODO support for lang= if we ever use it
	text = re.sub(r'\[codeblock](.*?)\[/codeblock]', r'```gdscript \1```', text, flags=re.DOTALL)
	# left and right brackets
	text = re.sub(r'\[lb]', r'[', text)
	text = re.sub(r'\[rb]', r']', text)
	# Convert line breaks [br] to actual newlines
	text = re.sub(r'\[br]\[br]', r'\n\n', text)
	# Two spaces in front to make md break the line
	text = re.sub(r'\[br]', r'  \n', text)

	# formatting specific to how we add descriptions
	# convert these in descriptions to sub-headlines
	text = re.sub(r'\*\*Parameters:\*\*', r'#### Parameters:\n', text)
	text = re.sub(r'\*\*Returns:\*\*', r'**Returns:**\n', text)
	text = re.sub(r'\*\*Examples:\*\*', r'#### Examples:\n', text)
	# Admonitions (https://regex101.com/r/DIcJ9K/2)
	# everything between opening === and closing === is an admonition
	# the first line is always discarded in favor of the default titles
	# optional: the type/color can be changed and a custom title can be set
	# by using a (technically invalid but invisible) empty bbcode [color] tag
	# example:
	# ===[br]
	# [b]Note:[color=note "A note on paths"][/color][/b][br]
	# Your extender script doesn't have to follow the same directory path as the vanilla file,
	# but it's good practice to do so.[br]
	# ===[br]
	text = re.sub(
		r'===.*?\n(?:[^=]*?\[color=(?P<type>\w+)[^\"]*?(?P<title>\".*?\")?]|.*?$).*?\n(?P<body>.*?)===',
		md_format_admonition,
		text, flags=re.DOTALL | re.MULTILINE
	)

	# colors
	text = re.sub(r'\[color=(.*?)](.*?)\[/color]', r'<span style="color: \1">\2</span>', text, flags=re.DOTALL)
	# Linking to other documentation
	# Godot built in classes
	text = re.sub(
		r'\[(\w+?)]',
		lambda match: f'[`#!gd {match.group(1)}`]({class_doc_link(match.group(1))})',
		text
	)
	# References to methods in the same file into links
	text = re.sub(
		r'\[method (\w+?)]',
		lambda match: f'[`#!gd {match.group(1)}()`]({class_doc_link(item_name=match.group(1))})',
		text
	)
	# Methods in other files
	text = re.sub(
		r'\[method (\w+?)\.(\w+?)]',
		lambda match: f'[`#!gd {match.group(1)}.{match.group(2)}()`]({class_doc_link(match.group(1), match.group(2))})',
		text
	)
	# Parameters are just like inline code
	text = re.sub(r'\[param (\w+?)]', r'`#!gd \1`', text)
	return text


def md_format_admonition(match):
	admonition_type = match.group('type') or "note"
	title = match.group('title') or ""
	admonition_type = f'\n\n!!! {admonition_type} {title}\n'  # admonition syntax
	content = match.group('body')

	# Split the content into lines and add a tab indent to each line
	indented_content = '\n'.join('\t' + line.strip() for line in content.splitlines())

	return admonition_type + indented_content + '\n'


def class_doc_link(class_name: str = None, item_name: str = None, item_type: str = "method"):
	if item_type == "member":
		item_type = "property"  # godot docs named it differently between url and xml for some reason

	anchor = ''
	if item_name is not None:
		anchor += f'#{item_type}-{item_name}'
	if class_name is None:  # local to script
		return anchor
	if "ModLoader" in class_name:
		return f'{pascal_to_snake_case(class_name)}.md{anchor}'

	docs_link = f'https://docs.godotengine.org/en/stable/classes/class_{class_name.lower()}.html'
	if item_name:
		docs_link += f'#class-{class_name.lower()}-{item_type}-{item_name.lower()}'
	return docs_link


# Function to convert XML to Markdown
def xml_to_markdown(xml_string):
	# Parse the XML
	root = ElementTree.fromstring(xml_string)

	# Extract class information
	class_name = root.get('name')
	inherits = root.get('inherits')

	md = ""

		# Process brief description for meta data
	brief_desc = root.find('brief_description')
	if brief_desc is not None and brief_desc.text.strip() != "":
		
		brief_desc_text = brief_desc.text.split("[br]")[0]

		if class_name == "ModLoaderMod":  # make it stand out a bit more in the list
			md += f"---\nstatus: new\ndescription: {bbcode_to_markdown(brief_desc_text)}\n---\n\n"
		else:
			md += f"---\ndescription: {bbcode_to_markdown(brief_desc_text)}\n---\n\n"

	md += f"# {class_name}\n"
	md += f"**Inherits**: {inherits}\n\n"

	# Process brief description
	if brief_desc is not None:
		md += f"\n{bbcode_to_markdown(brief_desc.text)}\n"

	# Process detailed description
	description = root.find('description')
	if description is not None and description.text.strip():
		md += f"## Description\n{bbcode_to_markdown(description.text)}\n\n"
	md += '<hr style="border-width: thick">\n\n'

	tutorials = root.find('tutorials')
	if tutorials is not None and len(tutorials.findall('tutorial')) > 0:
		md += "## Tutorials\n"
		for link in tutorials.findall('link'):
			title = link.get('title')
			url = link.text
			md += f"- [{title}]({url})\n"
		md += '<hr style="border-width: thick">\n'

	constants_md = get_variable_markdown(root, 'constants', 'constant')
	if constants_md is not None:
		md += "## Constants\n"
		md += constants_md

	properties_md = get_variable_markdown(root, 'members', 'member')
	if properties_md is not None:
		md += "## Properties\n"
		md += properties_md

	md += "## Method Descriptions\n"
	methods = root.findall('methods/method')
	for method in methods:
		method_name = method.get('name')
		if method_name.startswith('_'):
			continue

		# Return type
		returns = method.find('return')
		return_text = f"[`#!gd Variant`]({class_doc_link('Variant')})"
		if returns is not None:
			return_type = returns.get('type')
			if return_type == 'void':
				return_text = "void"
			else:
				return_text = f"[`#!gd {return_type}`]({class_doc_link(return_type)})"

		# static
		qualifiers = method.get('qualifiers', '')
		if qualifiers:
			qualifiers += " "

		# Parameters
		params = method.findall('param')
		params_text = ""
		if params:
			for param in params:
				param_name = param.get('name')
				param_type = param.get('type')
				params_text += f"{param_name}: [{param_type}]({class_doc_link(param_type)}), "
			params_text = params_text.removesuffix(", ")

		md += (
			# using a html code block here to be able to use links within
			f'### • {return_text} <code class="highlight">{method_name}({params_text})</code> {qualifiers}'
			# attribute list extension at the end ti prefix the anchor with method- and clean the table of contents
			f'{{#method-{method_name} data-toc-label=\'{method_name}\'}}\n'
		)

		description = method.find('description')
		if description is not None and description.text.strip():
			md += f"#### Description:\n{bbcode_to_markdown(description.text)}\n"

		# Separate methods by a line break
		md += "***\n"

	return md


def get_variable_markdown(xml_root, group_name, item_type):
	group = xml_root.find(group_name)
	if group is None:
		return None

	md = ""
	for item in group.findall(item_type):
		name = item.get('name')
		if name.startswith('_'):
			continue
		value = item.get('value')
		md += f"#### • `#!gd {name}`"
		if value is not None:
			md += f": `#!gd {value}`"
		md += f" {{{class_doc_link(None, name, item_type)} data-toc-label='{name}'}} \n"
	md += '\n<hr style="border-width: thick">\n\n'
	return md


# Read XML from a file and write Markdown to another file
def convert_file_to_markdown(input_file_path, output_file_path):
	print(f"Processing {input_file_path} -> {output_file_path}")
	# Read XML content from the input file
	with open(input_file_path, 'r', encoding='utf-8') as input_file:
		xml_content = input_file.read()

	# Convert XML to Markdown
	markdown_content = xml_to_markdown(xml_content)

	# Write the Markdown content to the output file
	with open(output_file_path, 'w', encoding='utf-8') as output_file:
		output_file.write(markdown_content)


def pascal_to_snake_case(text: str) -> str:
	return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


if __name__ == '__main__':
	xml_path = "gdscript_docs"
	md_path = "docs/api"

	# process all in the folder
	for file in os.listdir(xml_path):
		if not file.endswith(".xml"):
			continue

		filename = file.removesuffix(".xml")
		# ignore inner classes
		if "." in filename:
			filename = filename.split(".", 1)[-1]

		convert_file_to_markdown(
			f"{xml_path}/{file}",
			f"{md_path}/{pascal_to_snake_case(filename)}.md"
		)
