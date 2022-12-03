import os

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "input.txt")

scores = ["loss", "draw", "win"]
# rock, paper, scissors
my_signals = ["X", "Y", "Z"]
outcome = {
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}
# rock, paper, scissors
elf_signals = ["A", "B", "C"]

if __name__ == "__main__":
    score = 0
    with open(input_file) as f:
        for line in f:
            selections = line.split()
            elf_throw = elf_signals.index(selections[0])
            # ----------- task 1 ------
            my_throw = my_signals.index(selections[1])
            # -------------------------
            # ----------- task 2 ------
            # needed_outcome = outcome.get(selections[1])
            # if needed_outcome == "win":
            #     my_throw = (elf_throw + 1) % len(my_signals)
            # elif needed_outcome == "draw":
            #     my_throw = elf_throw
            # elif needed_outcome == "loss":
                # my_throw = (elf_throw - 1) % len(my_signals)
            # --------------------------
            signal_score = my_throw + 1
            if elf_throw == my_throw:
                result_score = scores.index("draw")*3
            elif elf_throw > my_throw:
                result_score = scores.index("loss")*3
                if elf_throw == len(elf_signals)-1 and my_throw == 0:
                    result_score = scores.index("win")*3
            elif elf_throw < my_throw:
                result_score = scores.index("win")*3
                if my_throw == len(my_signals)-1 and elf_throw == 0:
                    result_score = scores.index("loss")*3
            else:
                print(f"missad case: elf: {selections[0]}, me: {selections[1]}")
            print(signal_score + result_score)
            score = score + signal_score + result_score
        else:
            print(":)")
    print(f"score: {score}")