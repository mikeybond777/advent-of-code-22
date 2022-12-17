from utilities import *
import os
import numpy as np

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
    '''
    Move stacks based on the instructions in the puzzle input (day 5)
    :return:
    '''

    stacks_path = os.getcwd() + '\input_day5.txt'
    lines = text_file_to_lines(stacks_path)

    # Sort the stacks into lists.
    # 9 is the number for the first bit.

    crate_lists = [[], [], [], [], [], [], [], [], []]

    # For each line at top
    for index in range(8):
        line = lines[8-index-1]
        print(line)
        index_3 = 0

        # Get each letter and position for each line.
        for index_2 in range(1, len(line), 4):
            current_letter = line[index_2]
            if current_letter != ' ':
                crate_lists[index_3].append(current_letter)
            index_3 += 1

    # Crate lists should be full and ready to go.
    print(crate_lists)

    # Carry out the instructions.
    for index in range(10, len(lines)):
        line = lines[index]
        print(line)

        # Format the instructions
        line_split = line.split(' ')
        num_to_move = int(line_split[1])
        place_to_move_from = int(line_split[3])-1
        place_to_move_to = int(line_split[5])-1

        crate_column = crate_lists[place_to_move_from]
        new_crate_column, crates_to_move = split_list(crate_column, len(crate_column)-num_to_move)

        # Reverse the crates to move (hide this line to get the second part)
        crates_to_move = list(reversed(crates_to_move))

        # Update the new columns
        crate_lists[place_to_move_from] = new_crate_column
        crate_lists[place_to_move_to] += crates_to_move

        print(crate_lists)

    # Get the last thing in each stack.
    final_crates = ''

    for stack in crate_lists:

        final_crate = stack[-1]
        final_crates += final_crate

    print(final_crates)

def tuning_trouble():
    '''
    Finds the first 4 unique characters.
    :return:
    '''

    tuning_stack_path = os.getcwd() + '\input_day6.txt'
    lines = text_file_to_lines(tuning_stack_path)

    # Get the string of unique characters and the index of where those unique characters start.
    characters, index = unique_string(lines[0], 4)

    print(characters, index)

def no_space_left_on_device():
    '''
    Navigate directories to find the total sum. Day 7
    :return:
    '''

    searching_dirs = os.getcwd() + '\input_day7.txt'
    lines = text_file_to_lines(searching_dirs)

    # Path containing the current directory
    current_dir = ''
    # Dictionary containing all directories with the size.
    directory_sizes_dict = {}
    # Total data being used on the harddrive.
    total_size_used = 0

    for index in range(len(lines)):
        print(current_dir)

        line = lines[index]
        line_split = line.split(' ')

        # If the next line is a cd change the current directory to something else.
        if line.find('cd ') != -1:
            dir_to_change = line_split[-1]

            if dir_to_change == '..':
                current_dir = get_above_directory(current_dir)
            else:
                if dir_to_change != '/':
                    if current_dir != '/':
                        current_dir += '/' + dir_to_change
                    else:
                        current_dir += dir_to_change
                else:
                    current_dir = '/'

        elif line_split[0].isnumeric():

            data_to_add = int(line_split[0])
            total_size_used += data_to_add

            # Create a new directory entry with the size of the directory if it does not exist already, else add.
            if current_dir not in directory_sizes_dict.keys():
                directory_sizes_dict[current_dir] = data_to_add
            else:
                directory_sizes_dict[current_dir] += data_to_add

            # Make sure to also go back through the path to add the data size to upper directories too
            current_temp_dir = current_dir

            for index_2 in range(len(current_dir.split('/'))):
                current_temp_dir = get_above_directory(current_temp_dir)

                if current_temp_dir not in list((directory_sizes_dict.keys())):
                    directory_sizes_dict[current_temp_dir] = data_to_add
                else:
                    directory_sizes_dict[current_temp_dir] += data_to_add

    # Get the total data for entries less than 100000
    total_data = 0

    for entry in list(directory_sizes_dict.keys()):
        dir_data = directory_sizes_dict[entry]

        if dir_data <= 100000:
            total_data += dir_data

    print(directory_sizes_dict)
    print(total_data)

    #PART2

    # Find the smallest directory that is bigger than to 30000000
    directory_sizes = list(directory_sizes_dict.values())

    # Get the total size being occupied atm.

    # Work out how much space we'll need
    total_size_free = 70000000 - total_size_used
    space_required = 30000000 - total_size_free

    print(space_required, 'SPACE')

    # Find directories we can delete that will give us this space.
    directory_sizes_filtered = []

    for directory_size in directory_sizes:
        if directory_size >= space_required:
            directory_sizes_filtered.append(directory_size)

    print(directory_sizes_filtered)
    print(min(directory_sizes_filtered))


def treetop_tree_house():
    '''
    Find the number of trees visible in the grid.
    :return:
    '''

    tree_heights = os.getcwd() + '\input_day8.txt'
    lines = text_file_to_lines(tree_heights)

    # Initialize a numpy array
    row_lists = []

    for index in range(len(lines)):
        row = lines[index]
        row_list = [x for x in row]
        row_lists.append(row_list)

    grid_array = np.array(row_lists, dtype='i')

    # Get the size of the grid
    num_columns, num_rows = grid_array.shape
    visible_trees_dict = {}
    tree_scenic_scores = []

    # Iterate through every value
    for index_2 in range(num_rows):
        for index_3 in range(num_columns):

            tree_coordinates = (index_3, index_2)
            tree_height = grid_array[index_2, index_3]

            # If we are on the edge of the grid add the coordinates
            if tree_coordinates[0] == 0 or tree_coordinates[0] == num_columns - 1 or tree_coordinates[1] == 0 \
                or tree_coordinates[1] == num_rows - 1:
                visible_trees_dict[tree_coordinates] = tree_height
                continue

            # Get the current tree height and all values in the row
            current_row = grid_array[index_2]

            # Get lists of each side of the current tree
            trees_left = current_row[0:tree_coordinates[0]]
            trees_right = current_row[tree_coordinates[0]+1:]
            trees_above = grid_array[0:tree_coordinates[1], tree_coordinates[0]]
            trees_below = grid_array[tree_coordinates[1]+1:, tree_coordinates[0]]

            tree_scenic_score = (where_found_max(tree_height, np.flip(trees_left)) + 1) * \
                                (where_found_max(tree_height, trees_right) + 1) * \
                                (where_found_max(tree_height, np.flip(trees_above)) + 1) * \
                                (where_found_max(tree_height, trees_below) + 1)

            tree_scenic_scores.append(tree_scenic_score)

            # Check each direction to see if obstructed
            if tree_height > max(trees_left) or tree_height > max(trees_right) or tree_height > max(trees_above) \
                    or tree_height > max(trees_below):
                visible_trees_dict[tree_coordinates] = tree_height

    print(len(visible_trees_dict.keys()))
    print(max(tree_scenic_scores))

treetop_tree_house()
