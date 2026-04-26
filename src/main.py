from copy_static import copy_static
from generate_page import generate_pages_recursive
import os

def main():
    copy_static()

    content_dir = os.path.join(os.getcwd(), 'content')
    public_dir = os.path.join(os.getcwd(), "public")
    template_path = os.path.join(os.getcwd(), 'template.html')

    generate_pages_recursive(content_dir, template_path, public_dir)

    print("Site generation complete!")

main()
