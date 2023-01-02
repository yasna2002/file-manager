# DS Final Project
import os
from collections import defaultdict
from zipfile import ZipFile


class Stack:
    data = []
    size = 0

    def push(self, e):
        self.data.append(e)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.data.pop()

    def top(self):
        return self.data[-1]


files_added_stack = Stack()


def unzip():  # unzipping the main zip file
    with ZipFile("D:\\programs\\Github\\ds-project-olympians-ii\\Main.zip", 'r') as zObject:
        os.mkdir(path="D:/programs/Github/ds-project-olympians-ii/Main")  # unzips here

        zObject.extractall(path="D:\\programs\\Github\\ds-project-olympians-ii\\Main")


def find_dirs(root_dir, year_dict):  # finding all folders
    for file in os.listdir(root_dir):  # getting all the files and folders
        folder = os.path.join(root_dir, file)
        if os.path.isdir(folder):  # finding the folders
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
    print("Enter the name of file completely to delete : ")
    file_fullname = input()
    date = file_fullname.split(".")[1]
    format = file_fullname.split(".")[2]

    file_exist = False  # checks whether the file existed or not.
    if os.path.isdir(root_dir + "/" + date):
        if "jpg" in format or "png" in format or "gif" in format or "jpeg" in format:
            for file in os.listdir(root_dir + "/" + date + "/photo"):
                if file.split(".")[0] == file_fullname.split(".")[0]:
                    destination_path = root_dir + "/" + date + "/photo"
                    os.remove(destination_path + "/" + file_fullname)
                    file_exist = True
                    if len(os.listdir(destination_path)) == 0:
                        os.rmdir(destination_path)
        if "mp4" in format or "mov" in format or "mkv" in format or "avl" in format:
            for file in os.listdir(root_dir + "/" + date + "/video"):
                if file.split(".")[0] == file_fullname.split(".")[0]:
                    destination_path = root_dir + "/" + date + "/video"
                    os.remove(destination_path + "/" + file_fullname)
                    file_exist = True
                    if len(os.listdir(destination_path)) == 0:
                        os.rmdir(destination_path)
        if "wav" in format or "aiff" in format:
            for file in os.listdir(root_dir + "/" + date + "/voice"):
                if file.split(".")[0] == file_fullname.split(".")[0]:
                    destination_path = root_dir + "/" + date + "/voice"
                    os.remove(destination_path + "/" + file_fullname)
                    file_exist = True
                    if len(os.listdir(destination_path)) == 0:
                        os.rmdir(destination_path)
        if "txt" in format:
            for file in os.listdir(root_dir + "/" + date + "/text"):
                if file.split(".")[0] == file_fullname.split(".")[0]:
                    destination_path = root_dir + "/" + date + "/text"
                    os.remove(destination_path + "/" + file_fullname)
                    file_exist = True
                    if len(os.listdir(destination_path)) == 0:
                        os.rmdir(destination_path)
        if "pdf" in format:
            for file in os.listdir(root_dir + "/" + date + "/pdf"):
                if file.split(".")[0] == file_fullname.split(".")[0]:
                    destination_path = root_dir + "/" + date + "/pdf"
                    os.remove(destination_path + "/" + file_fullname)
                    file_exist = True
                    if len(os.listdir(destination_path)) == 0:
                        os.rmdir(root_dir + "/" + date)

    if file_exist:
        print("File Deleted!")
    else:
        print("File not found!")


def file_adder(root_dir):
    global destination
    print("name of the file to add: ")
    name = input()
    print("date of the file: ")
    date = input()
    if int(date) <= 2022:
        print("format of the file: ")
        format = input()

        fullName = name + "." + date + "." + format

        open(fullName, "x")
        path = os.path.join("D:\programs\Github\ds-project-olympians-ii", fullName)

        if not os.path.isdir(root_dir + "/" + date):
            os.mkdir(root_dir + "/" + date)
        if "jpg" in format or "png" in format or "gif" in format or "jpeg" in format:
            if not os.path.isdir(root_dir + "/" + date + "/photo"):
                os.mkdir(root_dir + "/" + date + "/photo")
            destination = os.path.join(root_dir + "/" + date + "/photo", fullName)
        if "mp4" in format or "mov" in format or "mkv" in format or "avl" in format:
            if not os.path.isdir(root_dir + "/" + date + "/video"):
                os.mkdir(root_dir + "/" + date + "/video")
            destination = os.path.join(root_dir + "/" + date + "/video", fullName)
        if "wav" in format or "aiff" in format:
            if not os.path.isdir(root_dir + "/" + date + "/voice"):
                os.mkdir(root_dir + "/" + date + "/voice")
            destination = os.path.join(root_dir + "/" + date + "/voice", fullName)
        if "txt" in format:
            if not os.path.isdir(root_dir + "/" + date + "/text"):
                os.mkdir(root_dir + "/" + date + "/text")
            destination = os.path.join(root_dir + "/" + date + "/text", fullName)
        if "pdf" in format:
            if not os.path.isdir(root_dir + "/" + date + "/pdf"):
                os.mkdir(root_dir + "/" + date + "/pdf")
            destination = os.path.join(root_dir + "/" + date + "/pdf", fullName)

        os.rename(path, destination)

        files_added_stack.push([fullName, 1])

        print("File created!")
    else:
        print("date invalid!")


def redo():
    temp = files_added_stack.pop()  # gets the last file

    f_name = os.path.basename(temp[0]).split('/')[-1].split('.')[0]
    date = os.path.basename(temp[0]).split('/')[-1].split('.')[1]
    format = os.path.basename(temp[0]).split('/')[-1].split('.')[2]

    name = f_name + "(" + str(temp[1]) + ")" + "." + date + "." + format  # adds a 1,2,3... at the end of the name

    open(name, "x")  # recreating the last file
    path = os.path.join("D:\programs\Github\ds-project-olympians-ii", name)

    if "jpg" in format or "png" in format or "gif" in format or "jpeg" in format:
        destination_path = os.path.join(root_dir + "/" + date + "/photo", name)
    if "mp4" in format or "mov" in format or "mkv" in format or "avl" in format:
        destination_path = os.path.join(root_dir + "/" + date + "/video", name)
    if "wav" in format or "aiff" in format:
        destination_path = os.path.join(root_dir + "/" + date + "/voice", name)
    if "txt" in format:
        destination_path = os.path.join(root_dir + "/" + date + "/text", name)
    if "pdf" in format:
        destination_path = os.path.join(root_dir + "/" + date + "/pdf", name)

    os.rename(path, destination_path)

    temp[1] = temp[1] + 1  # increases the index at the end of the name

    files_added_stack.push(temp)

    print("File recreated!")


def folder_creator(year_dict, root_dir):
    for key in sorted(year_dict.keys()):  # creating folders with date names
        os.mkdir(path="D:/programs/Github/ds-project-olympians-ii/Main/" + str(key))
        folder_path = "D:/programs/Github/ds-project-olympians-ii/Main/" + str(key)

        for value in range(len(year_dict[key])):
            if "jpg" in year_dict[key][value] or "png" in year_dict[key][value] or "gif" in year_dict[key][value] or "jpeg" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/photo"):
                    os.mkdir(path=folder_path + "/photo")  # creating folders with data type name
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
    root_dir = "D:/programs/Github/ds-project-olympians-ii/Main"
    year_dict = defaultdict(list)
    find_dirs(root_dir, year_dict)
    date_order(root_dir, year_dict)
    folder_creator(year_dict, root_dir)
    file_deleter(root_dir)
    # file_adder(root_dir)
    # redo()
