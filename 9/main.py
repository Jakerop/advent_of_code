import os

file_dir, _ = os.path.split(__file__)
file_path = os.path.join(file_dir, "input.txt")

def get_move_gen():
    with open(file_path) as f:
        for line in f:
            yield line.strip("\n").split()

def _adjust_tail_moving_right(head_pos, tail_pos):
    if head_pos[0] > tail_pos[0]+1:
        tail_pos[0] = tail_pos[0]+1
        if head_pos[1] != tail_pos[1]:
            tail_pos[1] += int(head_pos[1]-tail_pos[1])/abs(head_pos[1]-tail_pos[1])

def _adjust_tail_moving_left(head_pos, tail_pos):
    if head_pos[0] < tail_pos[0]-1:
        tail_pos[0] = tail_pos[0]-1
        if head_pos[1] != tail_pos[1]:
            tail_pos[1] += int(head_pos[1]-tail_pos[1])/abs(head_pos[1]-tail_pos[1])

def _adjust_tail_moving_up(head_pos, tail_pos):
    if head_pos[1] > tail_pos[1]+1:
        tail_pos[1] = tail_pos[1]+1
        if head_pos[0] != tail_pos[0]:
            tail_pos[0] += int(head_pos[0]-tail_pos[0])/abs(head_pos[0]-tail_pos[0])

def _adjust_tail_moving_down(head_pos, tail_pos):
    if head_pos[1] < tail_pos[1]-1:
        tail_pos[1] = tail_pos[1]-1
        if head_pos[0] != tail_pos[0]:
            tail_pos[0] += int(head_pos[0]-tail_pos[0])/abs(head_pos[0]-tail_pos[0])

def move_head(move, knot_positions):
    if move[0] == "R":
        knot_positions[0][0] += 1
    elif move[0] == "U":
        knot_positions[0][1] += 1
    elif move[0] == "L":
        knot_positions[0][0] -= 1
    elif move[0] == "D":
        knot_positions[0][1] -= 1

def excecute_partial_moves(move:list, knot_positions:list, tail_visits:set):
    for _ in range(int(move[1])):
        move_head(move, knot_positions)
        for i in range(1, len(knot_positions)):
            _adjust_tail_moving_right(knot_positions[i-1], knot_positions[i])
            _adjust_tail_moving_up(knot_positions[i-1], knot_positions[i])
            _adjust_tail_moving_left(knot_positions[i-1], knot_positions[i])
            _adjust_tail_moving_down(knot_positions[i-1], knot_positions[i])
        tail_visits.add(tuple(knot_positions[-1]))

def excecute_moves(knot_positions:list, tail_visits:set):
    move_generator = get_move_gen()
    while move := next(move_generator, False):
        excecute_partial_moves(move, knot_positions, tail_visits)

if __name__ == "__main__":
    ROPE_LEN = 2
    knot_positions = [[0,0] for _ in range(ROPE_LEN)]
    tail_visits = set()
    excecute_moves(knot_positions, tail_visits)
    print(len(tail_visits))
