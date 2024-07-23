import os, shutil
 
def from_static_to_public_dir(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if src_path == dest:
            continue
        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            from_static_to_public_dir(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)