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


def file_deletion(root_dir):
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
    date = input()
    if int(date) <= 2022:
        print("format of the file: ")
        format = input()

        fullName = name + "." + date + "." + format

        open(fullName, "x")
        path = os.path.join("D:\programs\Github\ds-project-olympians-ii", fullName)
        destination = os.path.join(root_dir, fullName)
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
    destination = os.path.join(root_dir, name)
    os.rename(path, destination)

    temp[1] = temp[1] + 1  # increases the index at the end of the name

    files_added_stack.push(temp)

    print("File recreated!")


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
    file_adder(root_dir)
    redo()
