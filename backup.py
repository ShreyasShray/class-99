import os
import shutil

source = input("Enter the source folder path: ")

destination = input("Enter the destination folder path: ")

source = source + "/"
destination = destination + "/"

allFiles = os.listdir(source)

for files in allFiles:
    shutil.copy((source + files), destination)