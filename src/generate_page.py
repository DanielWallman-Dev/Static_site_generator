import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path


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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensuring the destination directory exist
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(dir_path_content):
        # Full path to the current entry
        full_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(full_path) and entry.endswith('.md'):
            # Paths for reading and writing
            from_path = full_path
            to_path = os.path.join(dest_dir_path, entry.replace('.md', '.html'))
            
            
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

            # Write the resulting HTML to the destination path
            with open(to_path, 'w', encoding='utf-8') as html_file:
                html_file.write(final_content)
        
        elif os.path.isdir(full_path):
            # Recursive call to handle sub-directories
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_path, template_path, new_dest_dir)