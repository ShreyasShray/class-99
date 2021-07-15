import os
import shutil

path = input("Enter the path of the directory to be sorted: ")

allFiles = os.listdir(path)

for files in allFiles:
    name,ext = os.path.splitext(files)
    ext = ext[1:]
    if ext == "":
        continue

    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + files, path + "/" + ext + "/" + files)
    else:
        os.mkdir(path + "/" + ext)
        shutil.move(path + "/" + files, path + "/" + ext + "/" + files)
