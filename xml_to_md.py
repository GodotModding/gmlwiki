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
	text = re.sub(r'\[u](.*?)\[/u]', r'^^\1^^', text)
	# Convert code [code] to `code`, with inline highlight
	text = re.sub(r'\[code](.*?)\[/code]', r'`#!gd \1`', text)
	# Convert codeblock [codeblock] to triple backticks for code block
	# TODO support for lang=
	text = re.sub(r'\[codeblock](.*?)\[/codeblock]', r'```gdscript \1```', text, flags=re.DOTALL)
	# left and right brackets
	text = re.sub(r'\[lb]', r'[', text)
	text = re.sub(r'\[rb]', r']', text)
	# Convert line breaks [br] to actual newlines
	# Two spaces in front to make md break the line
	text = re.sub(r'\[br]', r'  \n', text)
	# Godot built in classes
	text = re.sub(
		r'\[(\w+?)]',
		lambda match: f'[`#!gd {match.group(1)}`]({class_doc_link(match.group(1))})',
		text
	)
	# References to methods in the same file into links
	text = re.sub(
		r'\[method (\w+?)]',
		lambda match: f'[`#!gd {match.group(1)}()`]({class_doc_link(method_name=match.group(1))})',
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

	# formatting specific to how we add descriptions
	# convert these in descriptions to sub-headlines
	text = re.sub(r'\*\*Parameters:\*\*', r'#### Parameters:\n', text)
	text = re.sub(r'\*\*Returns:\*\*', r'**Returns:**\n', text)
	text = re.sub(r'\*\*Examples:\*\*', r'#### Examples:\n', text)
	# Admonitions
	# considers > as starter for the type until a closing \n is met, all formatting needs to be discarded
	# everything after is considered the body until double [br] (which are replaced above with "  \n")
	text = re.sub(
		r'\s*>.*?(\w+).*?\n(.*?)  \n  \n',
		indent_admonition,
		text, flags=re.DOTALL
	)
	return text


def indent_admonition(match):
	before = match.group(1)  # '> note:' part
	before = f'\n\n!!! {before}\n'  # admonition syntax
	content = match.group(2)  # The content of the note, to indent

	# Split the content into lines and add a tab to each line
	indented_content = '\n'.join('\t' + line.strip() for line in content.splitlines())

	return before + indented_content + '\n'


def class_doc_link(class_name: str = None, method_name: str = None):
	anchor = ''
	if method_name is not None:
		anchor += f'#method-{method_name}'
	if class_name is None:  # local to script
		return anchor
	if "ModLoader" in class_name:
		return f'{pascal_to_snake_case(class_name)}.md{anchor}'

	docs_link = f'https://docs.godotengine.org/en/stable/classes/class_{class_name.lower()}.html'
	if method_name:
		docs_link += f'#class-{class_name.lower()}-method-{method_name.lower()}'
	return docs_link


# Function to convert XML to Markdown
def xml_to_markdown(xml_string):
	# Parse the XML
	root = ElementTree.fromstring(xml_string)

	# Extract class information
	class_name = root.get('name')
	inherits = root.get('inherits')

	md = f"# {class_name}\n"
	md += f"**Inherits**: {inherits}\n\n"

	# Process brief description
	brief_desc = root.find('brief_description')
	if brief_desc is not None:
		md += f"\n{bbcode_to_markdown(brief_desc.text)}\n"

	# Process detailed description
	description = root.find('description')
	if description is not None and description.text.strip():
		md += f"## Description\n{bbcode_to_markdown(description.text)}\n\n"
	md += '<hr style="border-width: thick">\n'

	tutorials = root.find('tutorials')
	if tutorials is not None and len(tutorials.findall('tutorial')) > 0:
		md += "## Tutorials\n"
		for link in tutorials.findall('link'):
			title = link.get('title')
			url = link.text
			md += f"- [{title}]({url})\n"
		md += '<hr style="border-width: thick">\n'

	constants = root.find('constants')
	if constants is not None:
		md += "## Constants\n"
		for constant in constants.findall('constant'):
			constant_name = constant.get('name')
			if constant_name.startswith('_'):
				continue
			constant_value = constant.get('value')
			# Unescape HTML entities (like "&quot;" to quotes)
			constant_value = re.sub(r'&quot;', '"', constant_value)
			md += f"- `#!gd {constant_name}`: `#!gd {constant_value}`\n"
		md += '<hr style="border-width: thick">\n'

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
			print(f"Skipping inner class {filename}")
			filename = filename.split(".", 1)[-1]

		convert_file_to_markdown(
			f"{xml_path}/{file}",
			f"{md_path}/{pascal_to_snake_case(filename)}.md"
		)
