from utilities import *
import os

def elf_with_most_calories():
    '''
    From a text doc of lists, get the elf with the most calories and the total of the top three. Day 1.
    :return:
    '''

    # Get each line from the input document of calories.
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

    # Reset the current index.
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

    # Print the total largest group of calories.
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
    Calculate the rock paper scissors scores from day 2.
    :return:
    '''

    # Get the strategy guide with the list of actions.
    strategy_guide_path = os.getcwd() + '\input_day2.txt'
    lines = text_file_to_lines(strategy_guide_path)

    translate_opponent = {'A':'ROCK', 'B':'PAPER', 'C':'SCISSORS'}
    translate_yourself = {'X':'ROCK', 'Y':'PAPER', 'Z':'SCISSORS'}

    your_score = 0

    # The game score when we read the columns as player 1 and player 2.
    for game in lines:
        p1_choice = translate_opponent[game[0]]
        p2_choice = translate_yourself[game[2]]

        outcome = rock_paper_scissors(p1_choice, p2_choice)
        your_score += calculate_rock_paper_scissors_score(p2_choice, outcome)
        print(1, game, p1_choice, p2_choice, outcome, calculate_rock_paper_scissors_score(p2_choice, outcome))

    print(your_score)

    # New translation dictionary and reset score.
    translate_outcome = {'X':'PLAYER1', 'Y':'DRAW', 'Z':'PLAYER2'}
    your_score = 0

    # The game score when we read the columns as player 1 and outcome.
    for game in lines:
        p1_choice = translate_opponent[game[0]]
        outcome = translate_outcome[game[2]]

        p2_choice = calculate_p2_choice(p1_choice, outcome)
        your_score += calculate_rock_paper_scissors_score(p2_choice, outcome)
        print(2, game, p1_choice, p2_choice, outcome, calculate_rock_paper_scissors_score(p2_choice, outcome))

    print(your_score)


def rucksack_organisation():
    '''
    Read the lists of what is in the rucksacks.
    :return:
    '''

    # Get the rucksack contents.
    rucksacks_path = os.getcwd() + '\input_day3.txt'
    rucksacks = text_file_to_lines(rucksacks_path)

    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum_of_priorities = 0

    # Find the matching thing in both compartments of each rucksack
    for rucksack in rucksacks:

        # Print what is in both compartments.
        total_num_items = len(rucksack)
        first_compartment, second_compartment = split_list(rucksack, int(total_num_items/2))

        # Get the matches in both compartments
        matches = set(first_compartment) & set(second_compartment)

        for match in matches:
            # Find returns where in the list the letter was
            where_found = priority.find(match) + 1
            sum_of_priorities += where_found

    print(sum_of_priorities)
    sum_of_priorities = 0

    for index in range(int(len(rucksacks)/3)):
        current_position = (index+1)*3

        rucksack_1 = rucksacks[current_position-3]
        rucksack_2 = rucksacks[current_position-2]
        rucksack_3 = rucksacks[current_position-1]

        matches = set(rucksack_1) & set(rucksack_2) & set(rucksack_3)

        for match in matches:
            where_found = priority.find(match) + 1
            sum_of_priorities += where_found

    print(sum_of_priorities)

def camp_cleanup():
    '''
    Compares the pairs of ranges to see whether one is contained in another or or if there is any overlap.
    :return:
    '''

    # Get ID inputs

    ids_path = os.getcwd() + '\input_day4.txt'
    lines = text_file_to_lines(ids_path)

    # The number of pairs in another
    pair_in_another_count = 0
    pair_overlaps_count = 0

    for line in lines:
        # Each line formatted like 4-4,5-6 so split to get each side
        elf_pair = line.split(',')

        # Convert each elf pair into a list
        elf1_range = range_to_list(elf_pair[0])
        elf2_range = range_to_list(elf_pair[1])

        #print(elf1_range, elf2_range)

        if compare_lists(elf1_range, elf2_range) == True or compare_lists(elf2_range, elf1_range):
            pair_in_another_count += 1

        matches = set(elf1_range) & set(elf2_range)
        if len(matches) > 0:
            pair_overlaps_count += 1

    print(pair_in_another_count)
    print(pair_overlaps_count)

def supply_stacks():

camp_cleanup()