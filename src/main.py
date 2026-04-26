from copy_static import copy_static
from generate_page import generate_pages_recursive
import os
import sys

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else '/'

    copy_static()

    content_dir = os.path.join(os.getcwd(), 'content')
    public_dir = os.path.join(os.getcwd(), "docs")
    template_path = os.path.join(os.getcwd(), 'template.html')

    generate_pages_recursive(content_dir, template_path, public_dir, base_path)

    print("Site generation complete!")

main()
