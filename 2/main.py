import os

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "input.txt")

scores = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}

my_signals = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

elf_signals = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

def get_signal_value(whomst, signal):
    if whomst == "me":
        return list(my_signals.keys()).index(signal)
    elif whomst == "elf":
        return list(elf_signals.keys()).index(signal)
    else:
        print("felskrivit")

if __name__ == "__main__":
    score = 0
    with open(input_file) as f:
        for line in f:
            selections = line.split()
            my_throw = get_signal_value("me", selections[1])
            elf_throw = get_signal_value("elf", selections[0])
            signal_score = my_throw + 1
            if elf_throw == my_throw:
                result_score = scores.get("draw")
            elif elf_throw > my_throw:
                result_score = scores.get("loss")
                elf_best_throw = list(elf_signals.keys())[-1]
                if elf_throw == get_signal_value("elf", elf_best_throw) and my_throw == 0:
                    result_score = scores.get("win")
            elif elf_throw < my_throw:
                result_score = scores.get("win")
                my_best_throw = list(my_signals.keys())[-1]
                if my_throw == get_signal_value("me", my_best_throw) and elf_throw == 0:
                    result_score = scores.get("loss")
            else:
                print(f"missad case: elf: {selections[0]}, me: {selections[1]}")
            print(signal_score + result_score)
            score = score + signal_score + result_score
    print(score)