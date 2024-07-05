import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.replace("# ", "").strip()
    raise Exception("Error, page has no header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")

    # Reading the files
    with open(from_path, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()
    
    with open(template_path, 'r', encoding='utf-8') as tpl_file:
        template_content = tpl_file.read()

    # Converting markdown to HTML and extracting the title
    HTML = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    
    # Replacing placeholders in the template
    final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", HTML)

    # Writing the final content to the destination path
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as dest_file:
        dest_file.write(final_content)