# DS Final Project
import os
from collections import defaultdict
from zipfile import ZipFile


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, e):
        self.data.append(e)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.data.pop()

    def top(self):
        return self.data[-1]


operations_stack = Stack()

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


def file_deleter():
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


def file_deleter_undo(dest):
    operations_stack.push([dest, "del"])
    os.remove(dest)

    print("File Deleted!")


def file_adder():
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

        operations_stack.push([destination, "add", 1])

        print("File created!")
    else:
        print("Date invalid!")


def file_adder_undo(file):
    name = os.path.basename(file).split('/')[-1].split('.')[0]
    date = os.path.basename(file).split('/')[-1].split('.')[1]
    format = os.path.basename(file).split('/')[-1].split('.')[2]

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

    operations_stack.push([destination, "add", 1])

    print("File created!")


def redo():
    temp = operations_stack.pop()  # gets the last file

    if temp[1] == "add":

        f_name = os.path.basename(temp[0]).split('/')[-1].split('.')[0]
        date = os.path.basename(temp[0]).split('/')[-1].split('.')[1]
        format = os.path.basename(temp[0]).split('/')[-1].split('.')[2]

        name = f_name + "(" + str(temp[2]) + ")" + "." + date + "." + format  # adds a 1,2,3... at the end of the name

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

        temp[2] = temp[2] + 1  # increases the index at the end of the name

        operations_stack.push(temp)
        print("File recreated!")
    else:
        print("nothing to redo!")


def undo():
    if operations_stack.size == 0:  # other stacks should be checked
        print("Nothing to undo!")
    elif operations_stack.top()[1] == "add":
        temp = operations_stack.pop()
        file_deleter_undo(temp[0])
    elif operations_stack.top()[1] == "del":
        temp = operations_stack.pop()
        file_adder_undo(temp[0])


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
    root_dir = "D:\\programs\\Github\\ds-project-olympians-ii\\Main"
    year_dict = defaultdict(list)
    find_dirs(root_dir, year_dict)
    # date_order(root_dir, year_dict)
    # file_deleter()
    folder_creator(year_dict, root_dir)
    file_adder()
    redo()
    undo()
