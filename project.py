# DS Final Project
import os
from zipfile import ZipFile

# unzipping the main zip file
def unzip():
    with ZipFile("E:\\Data Structure\\DS_Project\\Main.zip", 'r') as zObject:

        os.mkdir(path="E:/Data Structure/DS_Project/Main") #unzips here

        zObject.extractall(path="E:\\Data Structure\\DS_Project\\Main")

# finding all folders
def find_dirs(rootdir):
    for file in os.listdir(rootdir):
        folder = os.path.join(rootdir, file)
        if os.path.isdir(folder):
            #TODO
            for files in os.listdir(folder):
                old_dir = os.path.join(folder, files)
                new_dir = os.path.join(rootdir,files)
                os.rename(old_dir, new_dir)

            os.rmdir(folder)

            find_dirs(rootdir)

unzip()
rootdir = "E:\\Data Structure\\DS_Project\\Main"
find_dirs(rootdir)