import os
import time

file_dir, _ = os.path.split(__file__)
file_path = os.path.join(file_dir, "input.txt")


class Node():
    def __init__(self, name, parent=None, node_type=None, size=0):
        self.name = name
        self.children = list()
        self.parent = parent
        self.node_type = node_type
        self.size = 0
        self.update_size(size)

    def get_subdirs_of_limit_size(self, size_limit, result_list):
        size = self.size
        if size <= size_limit and self.node_type == "dir":
            result_list.append(size)
        for child in self.children:
            child.get_subdirs_of_limit_size(size_limit, result_list)

    def get_smallest_possible_subdir(self, size_limit):
        candidate = [self.name, self.size]
        for child in self.children:
            if child.size >= size_limit and child.node_type == "dir":
                child_dir_size = child.get_smallest_possible_subdir(size_limit)
                if child_dir_size[1] < candidate[1]:
                    candidate = child_dir_size
        return candidate

    def get_root(self):
        if self.parent is not None:
            return self.parent.get_root()
        return self

    def update_size(self, size_dif):
        self.size += size_dif
        try:
            self.parent.update_size(size_dif)
        except AttributeError:
            return


def parse_input(file_name):
    current_dir = Node("root", node_type="dir")
    with open(file_name) as f:
        for line in f:
            split_line = line.strip("\n").split()
            if split_line[0] == "$":
                if split_line[1] == "cd":
                    if split_line[2] == "/":
                        current_dir = current_dir.get_root()
                    elif split_line[2] == "..":
                        current_dir = current_dir.parent
                    else:
                        current_dir = next((child for child in current_dir.children if child.name == split_line[2]))
                    continue
                if split_line[1] == "ls":
                    continue
            else:
                if split_line[0].isnumeric():
                    current_dir.children.append(Node(split_line[1], current_dir, "file", int(split_line[0])))
                else:
                    current_dir.children.append(Node(split_line[1], current_dir, split_line[0]))
    return current_dir.get_root()


if __name__ == "__main__":
    dir_smaller_than_100000 = list()
    a = parse_input(file_path)
    a.get_subdirs_of_limit_size(100000, dir_smaller_than_100000)
    dir_sum = 0
    for dir_size in dir_smaller_than_100000:
        dir_sum += dir_size
    print(f"dir sum = {dir_sum}")
    needed_space = 30000000-(70000000-a.get_root().size)
    print(f"smallest_dir = {a.get_smallest_possible_subdir(needed_space)[1]}")