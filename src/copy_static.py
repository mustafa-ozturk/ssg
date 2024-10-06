import os
import shutil


def traverse_copy(src, dst):
    contents = os.listdir(src)

    for content in contents:
        path = os.path.join(src, content)
        if os.path.isfile(path) != True:
            os.mkdir(os.path.join(dst, content))
            traverse_copy(path, dst)
        else:
            print(f"copying {path} to {path.replace("static", "public")}")
            shutil.copy(path, path.replace("static", "public"))

def copy_src_to_clean_dest(src, dest):
    if os.path.exists(src) != True:
        raise Exception("Invalid src")
    if os.path.exists(dest) != True:
        os.mkdir(dest)
    else:
        # create a clean dir
        shutil.rmtree(dest)
        os.mkdir(dest)

    # recursively travers src directory
    traverse_copy(src, dest)
