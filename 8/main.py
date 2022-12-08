import os

file_dir, _ = os.path.split(__file__)
file_path = os.path.join(file_dir, "input.txt")

def parse_file(file_name):
    with open(file_name) as f:
        trees = [tree_row.strip("\n") for tree_row in f]
    return trees

def check_top(trees, tree_height, steps_taken, x_pos, y_pos):
    if y_pos == 0:
        return [True, steps_taken]
    elif tree_height <= trees[y_pos-1][x_pos]:
        return [False, steps_taken+1]
    else:
        return check_top(trees, tree_height, steps_taken+1, x_pos, y_pos-1)

def check_bottom(trees, tree_height, steps_taken, x_pos, y_pos):
    if y_pos == len(trees)-1:
        return [True, steps_taken]
    elif tree_height <= trees[y_pos+1][x_pos]:
        return [False, steps_taken+1]
    else:
        return check_bottom(trees, tree_height, steps_taken+1, x_pos, y_pos+1)

def check_left(trees, tree_height, steps_taken, x_pos, y_pos):
    if x_pos == 0:
        return [True, steps_taken]
    elif tree_height <= trees[y_pos][x_pos-1]:
        return [False, steps_taken+1]
    else:
        return check_left(trees, tree_height, steps_taken+1, x_pos-1, y_pos)

def check_right(trees, tree_height, steps_taken, x_pos, y_pos):
    if x_pos == len(trees[y_pos])-1:
        return [True, steps_taken]
    elif tree_height <= trees[y_pos][x_pos+1]:
        return [False, steps_taken+1]
    else:
        return check_right(trees, tree_height, steps_taken+1, x_pos+1, y_pos)

if __name__ == "__main__":
    trees = parse_file(file_path)
    visible_count = 0
    best_scenic_score = 0
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            tree_height = trees[row][col]
            result_top = check_top(trees, tree_height, 0, col, row)
            result_bottom = check_bottom(trees, tree_height, 0, col, row)
            result_left = check_left(trees, tree_height, 0, col, row)
            result_right = check_right(trees, tree_height, 0, col, row)
            if any((result_top[0], result_bottom[0], result_left[0], result_right[0])):
                visible_count += 1
            scenic_score = result_top[1]*result_bottom[1]*result_left[1]*result_right[1]
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score
    print(f"visible trees: {visible_count}")
    print(f"best scenic score: {best_scenic_score}")
