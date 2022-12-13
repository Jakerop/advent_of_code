import os
import sys

FILENAME = "input.txt"

def get_signal_pair():
    filedir = os.path.split(__file__)[0]
    with open(os.path.join(filedir, FILENAME)) as f:
        pairs = f.read().split("\n\n")
    for pair in pairs:
        signals = [eval(signal) for signal in pair.split("\n")]
        yield [signals[0], signals[1]]

def compare(left, right):
    for data_left, data_right in zip(left, right):
        if type(data_left) is int and type(data_right) is int:
            if data_left < data_right:
                return True
            elif data_left > data_right:
                return False
            else:
                continue
        if type(data_left) is not list:
            data_left = [data_left]
        if type(data_right) is not list:
            data_right = [data_right]
        compare_result = compare(data_left, data_right)
        if compare_result is None:
            continue
        else:
            return compare_result
    else:
        if len(left) == len(right):
            return None
        else:
            return len(left) < len(right)

def find_right_order():
    signal_pair_gen = get_signal_pair()
    i = 0
    idx_sum = 0
    while signal_pair := next(signal_pair_gen, False):
        i += 1
        left_pair = signal_pair[0]
        right_pair = signal_pair[1]
        if compare(left_pair, right_pair):
            idx_sum += i
    print(idx_sum)

def insert_signal_in_order(sorted_list: list, signal):
    for i, list_signal in enumerate(sorted_list):
        if compare(signal, list_signal):
            sorted_list.insert(i, signal)
            return
    else:
        sorted_list.append(signal)

def sort_signals():
    filedir = os.path.split(__file__)[0]
    with open(os.path.join(filedir, FILENAME)) as f:
        signals_str = f.read().replace("\n\n","\n").split("\n")
    signals = [eval(signal) for signal in signals_str]
    signals.append([[2]])
    signals.append([[6]])
    sorted_signals = []
    for signal in signals:
        insert_signal_in_order(sorted_signals, signal)
    return sorted_signals


if __name__ == "__main__":
    # ---- part 1 ------
    find_right_order()
    # ------------------
    # ---- part 2 ------
    sorted_signals = sort_signals()
    idx_2 = sorted_signals.index([[2]])+1
    idx_6 = sorted_signals.index([[6]])+1
    for signal in sorted_signals:
        print(signal)
    decoder_key = idx_2 * idx_6
    print(decoder_key)
    # ------------------
