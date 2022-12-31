# DS Final Project
import os
from zipfile import ZipFile


def unzip(): # unzipping the main zip file
    with ZipFile("E:\\Data Structure\\DS_Project\\Main.zip", 'r') as zObject:
        os.mkdir(path="E:/Data Structure/DS_Project/Main")  # unzips here

        zObject.extractall(path="E:\\Data Structure\\DS_Project\\Main")


def find_dirs(root_dir, year_dict): # finding all folders
    for file in os.listdir(root_dir):  # getting all the files and folders
        folder = os.path.join(root_dir, file)
        if os.path.isdir(folder):  # finding the folders
            # TODO
            for files in os.listdir(folder):  # getting all the files in the folder
                old_dir = os.path.join(folder, files)
                new_dir = os.path.join(root_dir, files)
                os.rename(old_dir, new_dir)  # changing dir of files

            os.rmdir(folder)  # deleting the folder

            find_dirs(root_dir)


if __name__ == '__main__':
    unzip()
    root_dir = "E:\\Data Structure\\DS_Project\\Main"
    year_dict = {}
    find_dirs(root_dir, year_dict)
