import os
from pathlib import Path
import shutil
from markdownconverter import extract_title, markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    src_dir_contents = os.listdir(dir_path_content)
    for entry in src_dir_contents:
        file_or_dir = os.path.join(dir_path_content, entry)
        if os.path.isfile(file_or_dir):
            print(str(file_or_dir))
            file_name = entry.split(".")[0]
            dest = os.path.join(dest_dir_path, f"{file_name}.html")
            generate_page(file_or_dir, template_path, dest)
        else:
            dest = os.path.join(dest_dir_path, entry)
            print("copying from", str(file_or_dir))
            print("copying to", str(dest))
            os.mkdir(dest)
            generate_pages_recursive(file_or_dir, template_path, dest)


def generate_page(from_path, template_path, dest_path):
    template_contents = ""
    markdown_contents = ""
    with open(template_path, 'r') as template_file:
        template_contents = template_file.read()
    with open(from_path, 'r') as from_file:
        markdown_contents = from_file.read()
    title = extract_title(markdown_contents)
    template_contents = template_contents.replace("{{ Title }}", title)
    html = markdown_to_html_node(markdown_contents).to_html()
    template_contents = template_contents.replace("{{ Content }}", html)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(template_contents)


def copy_static_to_public():
    clear_public_dir()
    path_to_public = Path("./public")
    path_to_static = Path("./static")
    copy_path_rec(path_to_static, path_to_public)

def clear_public_dir():
    path_to_public = Path("./public")
    print(f"clearing dir {path_to_public}")
    public_dir_contents = os.listdir(path_to_public)
    for entry in public_dir_contents:
        file_or_dir = os.path.join(path_to_public, entry)
        if os.path.isfile(file_or_dir):
            os.remove(file_or_dir)
        else:
            shutil.rmtree(file_or_dir)

def copy_path_rec(path_to_src, path_to_dest):
    print(f"copying from {path_to_src} to {path_to_dest}")
    src_dir_contents = os.listdir(path_to_src)
    for entry in src_dir_contents:
        file_or_dir = os.path.join(path_to_src, entry)
        if os.path.isfile(file_or_dir):
            print(str(file_or_dir))
            shutil.copy(file_or_dir, path_to_dest)
        else:
            dest = os.path.join(path_to_dest, entry)
            print("copying from", str(file_or_dir))
            print("copying to", str(dest))
            os.mkdir(dest)
            copy_path_rec(file_or_dir, dest)

