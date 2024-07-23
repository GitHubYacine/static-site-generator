from textnode import TextNode
from file_utils import from_static_to_public_dir
from gencontent import generate_pages_recursive
import os

dest = '/home/yacine/static/public/'
src = '/home/yacine/static/'
dir_path_content = "./content"
template_path = "./template.html"


def main():
    from_static_to_public_dir(src, dest)
    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dest)

main()