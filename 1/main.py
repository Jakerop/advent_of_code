import os
import sys
def read_input():
    file = os.path.join(os.getcwd(), "input.txt")
    with open(file) as f:
        input = f.readlines()
    return input

def calories_total(food_list:list):
    elf_calories = []
    elf_calories_counter = 0
    for food in food_list:
        food = food.strip("\n")
        if food == "":
            elf_calories.append(elf_calories_counter)
            elf_calories_counter = 0
            continue
        elf_calories_counter += int(food)
    else:
        elf_calories.append(elf_calories_counter)
    return elf_calories

def find_most_food(cal_list:list, ignore):
    most_food = {
        "elf_id": None,
        "calories": 0
    }
    i = 0
    for calories in cal_list:
        if calories > most_food.get("calories") and i not in ignore:
            most_food["calories"] = calories
            most_food["elf_id"] = i
        i += 1
    return most_food

def find_3_most_food(cal_list:list):
    callories_sum = 0
    ignore_list = []
    for i in range(3):
        elfs = find_most_food(cal_list, ignore_list)
        ignore_list.append(elfs.get("elf_id"))
        callories_sum += elfs.get("calories")
    return callories_sum


if __name__ == "__main__":
    food_list = read_input()
    calories_list = calories_total(food_list)
    # elf_most_food = find_most_food(calories_list)
    # print(elf_most_food.get("calories"))
    more_elves = find_3_most_food(calories_list)
    print(more_elves)
