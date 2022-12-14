import os
from math import copysign, inf
# from matplotlib import pyplot as plt

FILENAME = "input.txt"

def parse_data_gen() -> list:
    filedir = os.path.split(__file__)[0]
    with open(os.path.join(filedir, FILENAME)) as f:
        stone_walls = f.read().split("\n")
    for stone_wall in stone_walls:
        corners_str = stone_wall.split(" -> ")
        corners_split_str = [corner.split(",") for corner in corners_str]
        corners = [tuple([int(x) for x in corner]) for corner in corners_split_str]
        yield corners

def mark_walls():
    walls = set()
    stone_walls_gen = parse_data_gen()
    while corners := next(stone_walls_gen, None):
        for c_start, c_end in zip(corners[:-1], corners[1:]):
            direction = int(copysign(1, c_end[0]-c_start[0]))
            for x in range(c_start[0], c_end[0], direction):
                walls.add((x, c_start[1]))
            direction = int(copysign(1, c_end[1]-c_start[1]))
            for y in range(c_start[1], c_end[1], direction):
                walls.add((c_start[0], y))
        walls.add(corners[-1])
    return walls

def move_sand(coords, walls, bottom, part):
    if coords[1]+1 >= bottom[1]:
        if part == 1:
            return bottom
        if part == 2:
            return coords
    down = (coords[0], coords[1]+1)
    if down not in walls:
        return move_sand(down, walls, bottom, part)
    down_left = (coords[0]-1, coords[1]+1)
    if down_left not in walls:
        return move_sand(down_left, walls, bottom, part)
    down_right = (coords[0]+1, coords[1]+1)
    if down_right not in walls:
        return move_sand(down_right, walls, bottom, part)
    return coords

def add_sand(dropfrom, walls, bottom, part):
    return move_sand(dropfrom, walls, bottom, part)

def fill_room(walls:set, part):
    dropfrom = (500, 0)
    bottom = (inf, max(walls, key=lambda y : y[1])[1]+1)
    top = dropfrom
    if part == 2:
        bottom = (bottom[0], bottom[1]+1)
    # plt.figure()
    # plt.scatter([x[0] for x in walls], [dropfrom[1]-y[1] for y in walls], c="b")
    i = 0
    while bottom[1] > (new_sand := add_sand(dropfrom, walls, bottom, part))[1] > top[1]:
        # plt.scatter([new_sand[0]], [dropfrom[1]-new_sand[1]], c="r")
        i += 1
        walls.add(new_sand)
    if new_sand == top:
        # plt.scatter([new_sand[0]], [dropfrom[1]-new_sand[1]], c="r")
        i+=1
        walls.add(new_sand)
    # plt.show()
    return i


if __name__ == "__main__":
    for part in [1, 2]:
        walls = mark_walls()
        print(fill_room(walls, part))
