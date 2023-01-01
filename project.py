# DS Final Project
import os
from collections import defaultdict
from zipfile import ZipFile
def unzip():  # unzipping the main zip file
    with ZipFile("D:\\programs\\Github\\ds-project-olympians-ii\\Main.zip", 'r') as zObject:
        os.mkdir(path="D:/programs/Github/ds-project-olympians-ii/Main")  # unzips here
        zObject.extractall(path="D:\\programs\\Github\\ds-project-olympians-ii\\Main")
def find_dirs(root_dir, year_dict):  # finding all folders
    for file in os.listdir(root_dir):  # getting all the files and folders
        folder = os.path.join(root_dir, file)
        if os.path.isdir(folder):  # finding the folders
            # TODO
            for files in os.listdir(folder):  # getting all the files in the folder
                old_dir = os.path.join(folder, files)
                new_dir = os.path.join(root_dir, files)
                os.rename(old_dir, new_dir)  # changing dir of files
                if os.path.isfile(new_dir):  # finding files between files and folders
                    date = os.path.basename(new_dir).split('/')[-1].split('.')[-2]
                    if int(date) <= 2022:
                        year_dict[date].append(files)  # creating a dictionary of files by date key
                    else:
                        os.remove(new_dir)  # remove a file with invalid date
            # dict(sorted(year_dict.items()))
            os.rmdir(folder)  # deleting the folder
            find_dirs(root_dir, year_dict)


def date_order(root_dir, year_dict):  # sorting files by date
    os.mkdir(path="D:/programs/Github/ds-project-olympians-ii/Main/folder")  # creating a temp folder
    temp = "D:/programs/Github/ds-project-olympians-ii/Main/folder"
    for key in sorted(year_dict.keys()):  # moving sorted files to the temp dir
        for file in range(len(year_dict[key])):
            old_dir = os.path.join(root_dir, year_dict[key][file])
            new_dir = os.path.join(temp, year_dict[key][file])
            os.rename(old_dir, new_dir)

    for key in sorted(year_dict.keys()):  # moving out sorted files to the main dir
        for file in range(len(year_dict[key])):
            old_dir = os.path.join(temp, year_dict[key][file])
            new_dir = os.path.join(root_dir, year_dict[key][file])
            os.rename(old_dir, new_dir)
    os.rmdir(temp)


if __name__ == '__main__':
    unzip()
    root_dir = "D:\\programs\\Github\\ds-project-olympians-ii\\Main"
    year_dict = defaultdict(list)
    find_dirs(root_dir, year_dict)
    date_order(root_dir, year_dict)