import os
from tqdm import tqdm
from queue import Queue, Empty

class Monkey():
    def __init__(self, id_number):
        self.id = id_number
        self.items = Queue()
        self.test_denominator = None
        self.monkey_true = None
        self.monkey_false = None
        self.operator = None
        self.operator_number = None
        self.inspections_done = 0

    def do_monkey_tests(self):
        try:
            while item := self.items.get(0):
                if self.operator_number == "old":
                    operator_number = item
                else:
                    operator_number = self.operator_number
                if self.operator == "+":
                    item += operator_number
                elif self.operator == "*":
                    item *= operator_number
                else:
                    print("ERORR BROTTALENA")
                # item = int(item / 3)
                if item % self.test_denominator == 0:
                    self.monkey_true.items.put(item)
                else:
                    self.monkey_false.items.put(item)
                self.inspections_done += 1
        except Empty:
            return

def find_monkey_business(monkey_list:list, number):
    monkey_list.sort(key=lambda x: x.inspections_done, reverse=True)
    monkey_business = 1
    for monkey in monkey_list[:number]:
        monkey_business *= monkey.inspections_done
    return monkey_business


def parse_file():
    file_dir, _ = os.path.split(__file__)
    file_path = os.path.join(file_dir, "example.txt")
    monkey_list = list()
    with open(file_path) as f:
        for line in f:
            if line == "\n":
                monkey = None
                continue
            parsed_line = line.strip("\n").split()
            if parsed_line[0] == "Monkey":
                monkey_number = int(parsed_line[1][0])
                monkeys = [monkey for monkey in monkey_list if monkey.id == monkey_number]
                if not monkeys:
                    monkey = Monkey(monkey_number)
                    monkey_list.append(monkey)
                else:
                    monkey = monkeys[0]
            elif parsed_line[0] == "Starting":
                for item in parsed_line[2:]:
                    monkey.items.put(int(item.strip(",")))
            elif parsed_line[0] == "Operation:":
                operator = parsed_line[-2]
                monkey.operator = operator
                if parsed_line[-1].isnumeric():
                    operator_number = int(parsed_line[-1])
                else:
                    operator_number = parsed_line[-1]
                monkey.operator_number = operator_number
            elif parsed_line[0] == "Test:":
                test_denominator = int(parsed_line[-1])
                monkey.test_denominator = test_denominator
            elif parsed_line[0] == "If":
                if parsed_line[1] == "true:":
                    true_monkey_id = int(parsed_line[-1])
                    monkeys_with_id = [_monkey for _monkey in monkey_list if _monkey.id == true_monkey_id]
                    if monkeys_with_id:
                        true_monkey = monkeys_with_id[0]
                    else:
                        true_monkey = Monkey(true_monkey_id)
                        monkey_list.append(true_monkey)
                    monkey.monkey_true = true_monkey
                if parsed_line[1] == "false:":
                    false_monkey_id = int(parsed_line[-1])
                    monkeys_with_id = [_monkey for _monkey in monkey_list if _monkey.id == false_monkey_id]
                    if monkeys_with_id:
                        false_monkey = monkeys_with_id[0]
                    else:
                        false_monkey = Monkey(false_monkey_id)
                        monkey_list.append(false_monkey)
                    monkey.monkey_false = false_monkey
    monkey_list.sort(key=lambda x: x.id)
    return monkey_list

if __name__ == "__main__":
    monkeys = parse_file()
    for i in tqdm(range(10000)):
        for monkey in monkeys:
            monkey.do_monkey_tests()
    print(find_monkey_business(monkeys, 2))
