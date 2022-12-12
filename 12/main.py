import os
from math import inf

input_file = os.path.join(os.path.split(__file__)[0], "input.txt")

def load_file(filename):
    with open(filename) as f:
        return [line.strip("\n") for line in f.readlines()]

class Node():
    def __init__(self, coords:tuple, height) -> None:
        self.coords = coords
        self.came_from = None
        self.g_score = inf
        self.f_score = inf
        self.height = height

    def __eq__(self, __o: object) -> bool:
        return __o == self.coords

def get_node_height_gen(nodes, seach_for_height):
    for row in nodes:
        for node in row:
            if node.height == seach_for_height:
                yield node

def calc_h(coords, end):
    return abs(coords[0]-end[0])+abs(coords[1]-end[1])

def get_d(current:Node, neighbour:Node):
    if ord(neighbour.height)-ord(current.height) > 1:
        return inf
    return 1


def get_node_neighbours(node, nodemap):
    neighbours = set()
    if node.coords[0] > 0:
        #up
        neighbours.add((node.coords[0]-1, node.coords[1]))
    if node.coords[0] < len(nodemap)-1:
        #down
        neighbours.add((node.coords[0]+1, node.coords[1]))
    if node.coords[1] > 0:
        #left
        neighbours.add((node.coords[0], node.coords[1]-1))
    if node.coords[1] < len(nodemap[node.coords[0]])-1:
        #right
        neighbours.add((node.coords[0], node.coords[1]+1))
    return neighbours

def get_nodemap():
    heightmap = load_file(input_file)
    nodemap = [[Node((i, j), heightmap[i][j]) for j in range(len(heightmap[i]))] for i in range(len(heightmap))]
    return nodemap

def reconstruct_path(last_node):
    past_node = last_node
    total_path = []
    while past_node := past_node.came_from:
        total_path.insert(0, past_node.coords)
    return total_path

def _a_star(start_node, nodemap):
    start_node.height = "a" if start_node.height == "S" else start_node.height
    end_node_gen = get_node_height_gen(nodemap, "E")
    end_node = next(end_node_gen)
    end_node.height = "z"
    start_node.g_score = 0
    start_node.f_score = calc_h(start_node.coords, end_node.coords)
    open_list = [start_node]
    while open_list:
        current = open_list.pop(0)
        if current == end_node:
            return reconstruct_path(current)
        for neighbour_coords in get_node_neighbours(current, nodemap):
            neighbour_node = nodemap[neighbour_coords[0]][neighbour_coords[1]]

            tentative_g_score = current.g_score+get_d(current, neighbour_node)
            if tentative_g_score < neighbour_node.g_score:
                neighbour_node.came_from = current
                neighbour_node.g_score = tentative_g_score
                neighbour_node.f_score = tentative_g_score + calc_h(neighbour_node.coords, end_node.coords)
                if neighbour_node not in open_list:
                    open_list.append(neighbour_node)
                    open_list.sort(key=lambda x: x.f_score)
    return None

def a_star():
    # ----- part 1 ------
    # nodemap = get_nodemap()
    # start_node_gen = get_node_height_gen(nodemap, "S")
    # start_node = next(start_node_gen)
    # return _a_star(start_node, nodemap)
    # ------------------
    # ----- part 2 -----
    shortest_a = inf
    start_from_char = "a"
    start_node_gen = get_node_height_gen(get_nodemap(), start_from_char)
    while start_node := next(start_node_gen, False):
        heightmap = load_file(input_file)
        nodemap = [[Node((i, j), heightmap[i][j]) for j in range(len(heightmap[i]))] for i in range(len(heightmap))]
        path = _a_star(start_node, nodemap)
        if path is None:
            continue
        path_len = len(path)
        if path_len < shortest_a:
            shortest_path = path
            shortest_a = path_len
    print(f"shortest path from {start_from_char} is {shortest_a}")
    return shortest_path


def printmap(steps):
    printmap = load_file(input_file)
    for i, row in enumerate(printmap):
        printmap[i] = list(row)
    for step in steps:
        printmap[step[0]][step[1]] = f"\033[1;36m{printmap[step[0]][step[1]].capitalize()}\033[m"
    for row in printmap:
        string = "".join(row)
        print(string)

if __name__ == "__main__":
    steps = a_star()
    printmap(steps)
    print(len(steps))
    
