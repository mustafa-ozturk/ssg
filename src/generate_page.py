import os
from htmlnode import markdown_to_html_node
from inline_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f" Generating page from {from_path} to {dest_path} using {template_path}")

    f = open(from_path, 'r', encoding="utf-8")
    markdown = f.read()
    f.close()

    f = open(template_path, 'r', encoding="utf-8")
    template = f.read()
    f.close()

    htmlnode = markdown_to_html_node(markdown)
    html = htmlnode.to_html()

    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", html)

    # write to dest path and create any directories needed
    # /public/blog/index.html
    # should check if public is a dir 
    # then should check if blog is a dir
    path = "."
    for section in dest_path.split('/'):
        path = f"{path}/{section}"
        if section.endswith(".html"):
            # no more directories to create
            break
        if os.path.exists(path):
            continue
        else:
            print("path doesn't exist", path)
            os.mkdir(path)


    print("writing to", dest_path)
    f = open(dest_path, 'w', encoding="utf-8")
    f.write(template)
    f.close()
    

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)

    for content in contents:
        path = os.path.join(dir_path_content, content)
        if os.path.isfile(path) != True:
            print("path:", path)
            generate_page_recursive(path, template_path, dest_dir_path)
        else:
            destination = path.replace("content", "public")
            destination = destination.replace(".md", ".html")
            print(f"generate_page({path}, {template_path}, {destination})")
            generate_page(path, template_path, destination)

