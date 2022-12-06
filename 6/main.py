import os

path, _  = os.path.split(__file__)
input_file = os.path.join(path, "input.txt")

def start_in_string(string:str):
    for i, char in enumerate(string):
        if (string[:i] + string[i+1:]).find(char) != -1:
            return False
    return True

def get_start_idx(msg_len):
    with open(input_file) as f:
        line = f.readline()
        for i in range(msg_len, len(line)):
            if start_in_string(line[i-msg_len:i]):
                return i

if __name__ == "__main__":
    print(f"part 1: {get_start_idx(4)}")
    print(f"part 2: {get_start_idx(14)}")