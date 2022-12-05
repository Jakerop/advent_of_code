import os
from queue import LifoQueue

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "input.txt")


def get_row():
    for row in open(input_file):
        yield row

def find_startrows(get_row_generator):
    rows = []
    row = next(get_row_generator)
    while not row[1].isnumeric():
        row = row.strip("\n")
        rows.append(row)
        row = next(get_row_generator)
    return rows

def get_start(get_row_generator):
    startrows = find_startrows(get_row_generator)
    stacks = [LifoQueue() for _ in range((len(startrows[0])+1)//4)]
    for row in reversed(startrows):
        row_crates = row[1::4]
        if any([value.isnumeric() for value in row_crates]):
            return stacks
        for i, crate in enumerate(row_crates):
            if crate == " ":
                continue
            stacks[i].put(crate)
    return stacks

def get_command(get_row_generator, limit = 10):
    row = next(get_row_generator)
    command = row.split()
    if len(command) != 6:
        if limit <= 0:
            print(":(")
        return get_command(get_row_generator, limit-1)
    return [int(value) for value in command[1::2]]

def execute_commands(stacks, get_row_generator):
    try:
        while True:
            command = get_command(get_row_generator)
            for i in range(command[0]):
                moved_box = stacks[command[1]-1].get()
                stacks[command[2]-1].put(moved_box)
    except StopIteration:
       return

def execute_commands_multiple_boxes(stacks, get_row_generator):
    try:
        while True:
            command = get_command(get_row_generator)
            moving_boxes = LifoQueue()
            for _ in range(command[0]):
                moving_boxes.put(stacks[command[1]-1].get())
            for _ in range(command[0]):
                stacks[command[2]-1].put(moving_boxes.get())
    except StopIteration:
       return

def get_top_crates(stacks):
    return [stack.get() for stack in stacks]

def get_top_crates_str(stacks):
    top_crates = get_top_crates(stacks)
    top_crates_str = ""
    for crate in top_crates:
        top_crates_str += crate
    return top_crates_str


if __name__ == "__main__":
    get_row_generator = get_row()
    stacks = get_start(get_row_generator)
    # ------ Task 1 ------
    # execute_commands(stacks, get_row_generator)
    # --------------------
    # ------ Task 2 ------
    execute_commands_multiple_boxes(stacks, get_row_generator)
    # --------------------
    print(get_top_crates_str(stacks))

