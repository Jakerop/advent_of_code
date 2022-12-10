import os


def get_cmd_gen():
    file_dir, _ = os.path.split(__file__)
    file_path = os.path.join(file_dir, "input.txt")
    with open(file_path) as f:
        for line in f:
            yield line.strip("\n").split()


def add_char_screen(screen:str, cycle, X):
    sprite_position = (X+1)%40
    if sprite_position-1 <= cycle%40 <= sprite_position+1:
        screen += "#"
    else:
        screen += "."
    return screen


if __name__ == "__main__":
    cmd_gen = get_cmd_gen()
    signal_strength = 0
    cycle = 0
    X = 1
    get_next_cmd = True
    screen = ""
    while True:
        cycle += 1
        screen = add_char_screen(screen, cycle, X)
        if (cycle-20) % 40 == 0:
            signal_strength += cycle*X
        if get_next_cmd:
            cmd = next(cmd_gen, False)
            if not cmd:
                break
        else:
            get_next_cmd = True
            if cmd[0] == "addx":
                X += int(cmd[1])
                continue
        if cmd[0] == "noop":
            continue
        if cmd[0] == "addx":
            get_next_cmd = False
    screen = "\n".join([screen[x:x+40] for x in range(0, len(screen), 40)])
    pretty_screen = " "+" ".join([screen[x:x+1] for x in range(0, len(screen), 1)])
    print(signal_strength)
    print(pretty_screen)