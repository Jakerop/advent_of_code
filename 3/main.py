import os

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "input.txt")

def get_prio(input:str):
    if input.isupper():
        prio = ord(input)-38
    else:
        prio = ord(input)-96
    return prio

def find_common(items:str):
    for item_1 in items[:int(len(items)/2)]:
        for item_2 in items[int(len(items)/2):]:
            if item_1 == item_2:
                return item_1
    print("no common found")
    return

def find_badge(bags:list):
    for item in bags[0]:
        if item in bags[1] and item in bags[2]:
            return item

if __name__ == "__main__":
    prio_sum = 0
    bags = [None, None, None]
    with open(input_file) as f:
        for i, line in enumerate(f):
            bags[i % 3] = line.strip("\n")
            if i % 3 != 2:
                continue
            common_item = find_badge(bags)
            item_prio = get_prio(common_item)
            prio_sum = prio_sum + item_prio
    print(prio_sum)
