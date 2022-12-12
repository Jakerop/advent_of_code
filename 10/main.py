import os
from math import fmod


def get_cmd_gen():
    file_dir, _ = os.path.split(__file__)
    file_path = os.path.join(file_dir, "input.txt")
    with open(file_path) as f:
        for line in f:
            yield line.strip("\n").split()


def add_char_screen(screen:str, cycle, X):
    # -1%40 = 39 and fmod(-1,40) = -1
    sprite_position = fmod(X, 40)
    # sprite_position = X%40
    if sprite_position-1 <= (cycle-1)%40 <= sprite_position+1:
        screen += "#"
    else:
        screen += "."
    return screen


def calc_signal_strength(cycle, signal_strength):
    if (cycle-20) % 40 == 0:
        signal_strength += cycle*X
    return signal_strength


def excecute_cmd(X):
    cmd_gen = get_cmd_gen()
    get_next_cmd = True
    while True:
        if get_next_cmd:
            cmd = next(cmd_gen)
            if cmd[0] == "addx":
                get_next_cmd = False
        else:
            get_next_cmd = True
            if cmd[0] == "addx":
                X += int(cmd[1])
        yield X


if __name__ == "__main__":
    signal_strength = 0
    cycle = 0
    X = 1
    screen = ""
    excecute_cmd_gen = excecute_cmd(X)
    while True:
        cycle += 1
        screen = add_char_screen(screen, cycle, X)
        signal_strength = calc_signal_strength(cycle, signal_strength)
        try:
            X = next(excecute_cmd_gen)
        except RuntimeError:
            break
    screen = "\n".join([screen[x:x+40] for x in range(0, len(screen), 40)])
    pretty_screen = " "+" ".join([screen[x:x+1] for x in range(0, len(screen), 1)])
    print(signal_strength)
    print(screen)
