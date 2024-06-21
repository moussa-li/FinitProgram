import os
import shutil
def move_file(old_path, new_path):
    src = old_path
    dst = os.path.join(new_path)
    # print('src:', src)
    # print('dst:', dst)
    shutil.move(src, dst)