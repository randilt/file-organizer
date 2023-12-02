# Author Randil Tharusha
# Project Python file organize

import os, shutil
path = r"D:\pyt"
# 1. check if there are any folders already existing inside the specified path.
# 2. check the filetypes of the files inside the folder
# 3. put into the correct folders.

files = os.listdir(path)

for file in files:
    print(file)