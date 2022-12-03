from utilities import *
import os

def elf_with_most_calories():
    '''
    From a text doc of lists, get the elf with the most calories and the total of the top three. Day 1.
    :return:
    '''

    calories_path = os.getcwd() + '\input.txt'
    lines = text_file_to_lines(calories_path)

    # Variables required for calculation.
    current_index = 0
    elf_count = 1
    elf_calorie_dict = {}
    elf_calorie_total_dict = {}

    # Initialise a dictionaries containing a list of elves
    for current_index in range(lines.count('')+1):
        elf_calorie_dict['elf' + str(current_index+1)] = []
        elf_calorie_total_dict['elf' + str(current_index+1)] = 0

    # Reset the current index
    current_index = 0

    # Sort list into a dictionary of elves and lists of number of calories they are carrying
    while current_index < len(lines):
        current_item = lines[current_index]
        if current_item == '':
            elf_count += 1
        else:
            elf_calorie_dict['elf' + str(elf_count)].append(current_item)
            elf_calorie_total_dict['elf' + str(elf_count)] += int(current_item)
        current_index += 1

    print(max(elf_calorie_total_dict.values()))

    # Variable required for top 3 elves calculation
    top_elves = {}
    temp_elf_calorie_total_dict = elf_calorie_total_dict
    #print(bubble_sort_dict(elf_calorie_total_dict))

    # Get the top three elves and their total calories.
    for current_index in range(3):
        current_top_elf_value = max(temp_elf_calorie_total_dict.values())
        current_top_elf = get_key_from_value(temp_elf_calorie_total_dict, current_top_elf_value)

        top_elves[current_top_elf] = current_top_elf_value

        temp_elf_calorie_total_dict.pop(current_top_elf)

    print(top_elves)
    print(sum_of_list(list(top_elves.values())))


def rock_paper_scissors_score():
    '''

    :return:
    '''
    strategy_guide_path = os.getcwd() + '\input_day2.txt'
    lines = text_file_to_lines(strategy_guide_path)

    print(lines)

rock_paper_scissors_score()