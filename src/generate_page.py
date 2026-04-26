from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os, re

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        content = file.read()

    with open(template_path, 'r') as file:
        template_content = file.read()

    html_content = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    page = template_content.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html_content)

    page = adjust_paths(page, basepath)

    with open(dest_path, "w") as file:
        file.write(page)

def adjust_paths(page_content, basepath):
    if not basepath.startswith('/'):
        basepath = '/' + basepath
    if not basepath.endswith('/'):
        basepath += '/'

    page_content = re.sub(r'href="/([^"]*)"', f'href="{basepath}\\1"', page_content)
    page_content = re.sub(r'src="/([^"]*)"', f'src="{basepath}\\1"', page_content)

    return page_content

def generate_pages_recursive(content_dir, template_path, public_dir, basepath):
    for root, dirs, files in os.walk(content_dir):
        relative_path = os.path.relpath(root, content_dir)

        for file in files:
            if file.endswith('.md'):
                markdown_file_path = os.path.join(root, file)

                relative_dest_dir = os.path.join(public_dir, relative_path)
                os.makedirs(relative_dest_dir, exist_ok=True)

                html_file_path = os.path.join(relative_dest_dir, file.replace('.md', '.html'))

                generate_page(markdown_file_path, template_path, html_file_path, basepath)
