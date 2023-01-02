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


def file_deleter(root_dir):
    print("name of the file you want to delete: ")
    name = input()

    cond = False  # checks whether the file existed or not.
    for files in os.listdir(root_dir):
        if name == os.path.basename(files).split('/')[-1].split('.')[0]:  # checks if the file name matched.
            direct = os.path.join(root_dir, files)
            os.remove(direct)
            cond = True
    if cond is True:
        print("File Deleted!")
    else:
        print("File not found!")


def file_adder(root_dir):
    print("name of the file to add: ")
    name = input()
    print("date of the file: ")
    date = int(input())
    if date <= 2022:
        print("format of the file: ")
        format = input()

        fullName = name + "." + str(date) + "." + format

        open(fullName, "x")
        path = os.path.join("D:\programs\Github\ds-project-olympians-ii", fullName)
        destination = os.path.join(root_dir, fullName)
        os.rename(path, destination)
    else:
        print("date invalid!")


def folder_creator(year_dict, root_dir):
    for key in sorted(year_dict.keys()):  # moving sorted files to the temp dir
        os.mkdir(path="D:/programs/Github/ds-project-olympians-ii/Main/" + str(key))
        folder_path = "D:/programs/Github/ds-project-olympians-ii/Main/" + str(key)

        for value in range(len(year_dict[key])):
            if "jpg" in year_dict[key][value] or "png" in year_dict[key][value] or "gif" in year_dict[key][value] or "jpeg" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/photo"):
                    os.mkdir(path=folder_path + "/photo")
                old_dir = os.path.join(root_dir, year_dict[key][value])
                new_dir = os.path.join(folder_path + "/photo", year_dict[key][value])
                os.rename(old_dir, new_dir)
            if "mp4" in year_dict[key][value] or "mov" in year_dict[key][value] or "mkv" in year_dict[key][value] or "avl" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/video"):
                    os.mkdir(path=folder_path + "/video")
                old_dir = os.path.join(root_dir, year_dict[key][value])
                new_dir = os.path.join(folder_path + "/video", year_dict[key][value])
                os.rename(old_dir, new_dir)
            if "wav" in year_dict[key][value] or "aiff" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/voice"):
                    os.mkdir(path=folder_path + "/voice")
                old_dir = os.path.join(root_dir, year_dict[key][value])
                new_dir = os.path.join(folder_path + "/voice", year_dict[key][value])
                os.rename(old_dir, new_dir)
            if "txt" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/text"):
                    os.mkdir(path=folder_path + "/text")
                old_dir = os.path.join(root_dir, year_dict[key][value])
                new_dir = os.path.join(folder_path + "/text", year_dict[key][value])
                os.rename(old_dir, new_dir)
            if "pdf" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/pdf"):
                    os.mkdir(path=folder_path + "/pdf")
                old_dir = os.path.join(root_dir, year_dict[key][value])
                new_dir = os.path.join(folder_path + "/pdf", year_dict[key][value])
                os.rename(old_dir, new_dir)


if __name__ == '__main__':
    unzip()
    root_dir = "D:\\programs\\Github\\ds-project-olympians-ii\\Main"
    year_dict = defaultdict(list)
    find_dirs(root_dir, year_dict)
    date_order(root_dir, year_dict)
    # file_deleter(root_dir)
    # file_adder(root_dir)
    folder_creator(year_dict, root_dir)
