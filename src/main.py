import os
import shutil
from copy_static import *
from generate_page import generate_page_recursive

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    copy_src_to_clean_dest("./static", "./public")
    generate_page_recursive("content", "template.html", "public")


main()
