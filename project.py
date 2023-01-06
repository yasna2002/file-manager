# DS Final Project
import os
from collections import defaultdict
from zipfile import ZipFile


class Tree:
    def __init__(self, data):
        self.data = data
        self.children: list[Tree] = []


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
files_added_stack = Stack()
file_tree_root = None


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


def date_order(year_dict):  # sorting files by date
    text_file = open("_sorted by date_.txt", "a")
    for key in sorted(year_dict.keys()):
        for value in range(len(year_dict[key])):
            text_file.write(year_dict[key][value] + "\n")
    text_file.close()


def type_order(year_dict):
    text_file = open("_sorted by type_.txt", "a")
    type_dict = defaultdict(list)
    for key in sorted(year_dict.keys()):
        for value in range(len(year_dict[key])):
            # print(year_dict[key][value].split(".")[2])
            if "png" in year_dict[key][value].split(".")[2]:  # photo
                type_dict[1].append(year_dict[key][value])
            if "jpeg" in year_dict[key][value].split(".")[2]:
                type_dict[2].append(year_dict[key][value])
            if "jpg" in year_dict[key][value].split(".")[2]:
                type_dict[3].append(year_dict[key][value])
            if "gif" in year_dict[key][value].split(".")[2]:
                type_dict[4].append(year_dict[key][value])
            if "mp4" in year_dict[key][value].split(".")[2]:  # movie
                type_dict[5].append(year_dict[key][value])
            if "mov" in year_dict[key][value].split(".")[2]:
                type_dict[6].append(year_dict[key][value])
            if "mkv" in year_dict[key][value].split(".")[2]:
                type_dict[7].append(year_dict[key][value])
            if "avl" in year_dict[key][value].split(".")[2]:
                type_dict[8].append(year_dict[key][value])
            if "wav" in year_dict[key][value].split(".")[2]:  # voice
                type_dict[9].append(year_dict[key][value])
            if "aiff" in year_dict[key][value].split(".")[2]:
                type_dict[10].append(year_dict[key][value])
            if "txt" in year_dict[key][value].split(".")[2]:  # text
                type_dict[11].append(year_dict[key][value])
            if "pdf" in year_dict[key][value].split(".")[2]:  # pdf
                type_dict[12].append(year_dict[key][value])

    for key in sorted(type_dict.keys()):
        for value in range(len(type_dict[key])):
            text_file.write(type_dict[key][value] + "\n")

    text_file.close()


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
    operations_stack.push([destination_path + "/" + file_fullname, "del"])
    if file_exist:
        print("File Deleted!")
    else:
        print("File not found!")


def file_deleter_undo(dest):
    operations_stack.push([dest, "del"])
    os.remove(dest)

    print("File Deleted!")


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

        operations_stack.push([destination, "add", 1])
        files_added_stack.push([fullName, 1])

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
            if "jpg" in year_dict[key][value] or "png" in year_dict[key][value] or "gif" in year_dict[key][
                value] or "jpeg" in year_dict[key][value]:
                if not os.path.isdir(folder_path + "/photo"):
                    os.mkdir(path=folder_path + "/photo")  # creating folders with data type name
                old_dir = os.path.join(root_dir, year_dict[key][value])
                new_dir = os.path.join(folder_path + "/photo", year_dict[key][value])
                os.rename(old_dir, new_dir)
            if "mp4" in year_dict[key][value] or "mov" in year_dict[key][value] or "mkv" in year_dict[key][
                value] or "avl" in year_dict[key][value]:
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


def tree_maker():
    global file_tree_root

    with ZipFile("D:\\programs\\Github\\ds-project-olympians-ii\\Main.zip", 'r') as zObject:
        os.mkdir(path="D:/programs/Github/ds-project-olympians-ii/Phase3")  # unzips here

        zObject.extractall(path="D:\\programs\\Github\\ds-project-olympians-ii\\Phase3")

    directory = "D:/programs/Github/ds-project-olympians-ii/Phase3"

    folder = os.path.join(directory, os.listdir(directory)[0])
    root = Tree(os.listdir(directory)[0])
    file_tree_root = root

    directory_tree(folder, root)


def directory_tree(path, root_node):
    file_in_dir_count = 0
    for file in os.listdir(path):
        fold = os.path.join(path, file)
        file_node = Tree(file)

        if os.path.isdir(fold):
            root_node.children.append(file_node)
            directory_tree(fold, file_node)
        else:
            date = file.split('.')[1]
            if int(date) > 2022:
                continue

            root_node.children.insert(file_in_dir_count, file_node)
            file_in_dir_count += 1


# Searches a folder name in the file tree structure with BFS
def search_folder(folder_name_to_find):
    if file_tree_root is None:
        raise Exception("file_tree_root is None. It seems that file tree structure is not initialized."
                        "Call tree_maker() first.")

    queue = [file_tree_root]

    while len(queue) != 0:
        item = queue.pop()
        if item.data == folder_name_to_find:
            return item

        for child in item.children:
            queue.append(child)

    return None


def traverse_tree_inorder(root: Tree | None):
    result = []

    if len(root.children) > 0:
        result = result + traverse_tree_inorder(root.children[0])

    result.append(root)

    for i in range(1, len(root.children)):
        result = result + traverse_tree_inorder(root.children[i])

    return result


def traverse_tree_preorder(root: Tree | None):
    result = [root]

    for child in root.children:
        result = result + traverse_tree_preorder(child)

    return result


def traverse_tree_postorder(root: Tree | None):
    result = []

    for child in root.children:
        result = result + traverse_tree_postorder(child)

    result.append(root)

    return result


def print_tree():
    print("Enter folder name: ")
    name = input()
    node = search_folder(name)
    if node is not None:
        print("Preorder: ", to_string_tree_traversal(traverse_tree_preorder(node)))
        print("Postorder: ", to_string_tree_traversal(traverse_tree_postorder(node)))
        print("Inorder: ", to_string_tree_traversal(traverse_tree_inorder(node)))
    else:
        print("Folder not found!")


def to_string_tree_traversal(path_list):
    final_str = ""
    for i, item in enumerate(path_list):
        final_str = final_str + (" * " if i > 0 else "") + str(item.data)
    return final_str


if __name__ == '__main__':
    unzip()
    # root_dir = "D:/programs/Github/ds-project-olympians-ii/Main"
    # year_dict = defaultdict(list)
    # find_dirs(root_dir, year_dict)
    # date_order(year_dict)
    # type_order(year_dict)
    # folder_creator(year_dict, root_dir)
    # file_deleter()
    # file_adder()
    # redo()
    # undo()
    tree_maker()
    print_tree()
