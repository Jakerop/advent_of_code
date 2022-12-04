import os

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "input.txt")

def convert_range(dash_range:str):
    endpoints = dash_range.split("-")
    set_range = set(range(int(endpoints[0]), int(endpoints[1])+1))
    return set_range

def count_subset(sets_list):
    subsets = 0
    for i, set1 in enumerate(sets_list[:-1]):
        for set2 in sets_list[i+1:]:
            if set1.issubset(set2):
                subsets += 1
            elif set2.issubset(set1):
                subsets += 1
    return subsets

def count_overlap(sets_list):
    overlaps = 0
    for i, set1 in enumerate(sets_list[:-1]):
        for set2 in sets_list[i+1:]:
            if set1.intersection(set2):
                overlaps += 1
    return overlaps

if __name__ == "__main__":
    with open(input_file) as f:
        section_subsets = 0
        section_overlaps = 0
        for line in f:
            elf_sections_txt = line.strip("\n").split(",")
            elf_sections = [None for x in elf_sections_txt]
            for i, section in enumerate(elf_sections_txt):
                elf_sections[i] = convert_range(section)
            section_subsets += count_subset(elf_sections)
            section_overlaps += count_overlap(elf_sections)
    print(f"subsets: {section_subsets}")
    print(f"overlaps: {section_overlaps}")
