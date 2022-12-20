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

def update_pos(coordinates, direction):
    '''
    Used by day 9 to update the position based on an input.
    :return:
    '''

    if direction == 'U':
        coordinates[1] += 1
    elif direction == 'D':
        coordinates[1] -= 1
    elif direction == 'L':
        coordinates[0] -= 1
    elif direction == 'R':
        coordinates[0] += 1

    return coordinates

def calc_tail(head_pos, tail_pos):
    '''
    Used by Day 9 part 2 to calculate the input of the tail
    :return:
    '''

    x_diff = head_pos[0] - tail_pos[0]
    y_diff = head_pos[1] - tail_pos[1]

    # If the head is at no more than 1 position away than the tail no need to move the tail
    if x_diff ** 2 <= 1 and y_diff ** 2 <= 1:
        return tail_pos
    # If x is 2 away then head in this direction
    elif x_diff ** 2 == 4:
        tail_pos[0] += int((x_diff / 2))
        # Need to accomodate diagonal positions too in this function
        if y_diff ** 2 == 4:
            tail_pos[1] += int((y_diff / 2))
        elif y_diff ** 2 == 1:
            tail_pos[1] = head_pos[1]
    # If y is 2 away then head in this direction
    elif y_diff ** 2 == 4:
        tail_pos[1] += int((y_diff / 2))
        # Need to accomodate diagonal positions too in this function
        if x_diff ** 2 == 4:
            tail_pos[0] += int((x_diff / 2))
        elif x_diff ** 2:
            tail_pos[0] = head_pos[0]

    return tail_pos

def rope_bridge():
    '''
    Day 9 - find the places where the tail of a rope has been when the head has been moving about.
    '''

    move_instructions = os.getcwd() + '\input_day9.txt'
    lines = text_file_to_lines(move_instructions)

    # PART 1

    head_pos = [0, 0]
    tail_pos = [0, 0]

    # List of tuples containing everywhere the tail has been
    tail_positions = []
    tail_positions.append(tuple(tail_pos))

    for line in lines:

        # Split the line to get the full instruction
        line_split = line.split(' ')
        direction = line_split[0]
        number = int(line_split[1])

        for execution in range(number):

            head_pos = update_pos(head_pos, direction)

            # Now calculate position of tail

            x_diff = head_pos[0] - tail_pos[0]
            y_diff = head_pos[1] - tail_pos[1]

            # If the head is at no more than 1 position away than the tail continue
            if x_diff ** 2 <= 1 and y_diff ** 2 <= 1:
                continue
            # If x is 2 away then head in this direction
            elif x_diff ** 2 == 4:
                tail_pos[0] += int((x_diff/2))
                # If x was 2 away and we are not in the same column then move to the same column
                if y_diff ** 2 < 1:
                    tail_pos[1] = head_pos[1]
            # If y is 2 away then head in this direction
            elif y_diff ** 2 == 4:
                tail_pos[1] += int((y_diff/2))
                # If y was 2 away and we are not in the same column then move to the same column
                if x_diff ** 2 < 1:
                    tail_pos[0] = head_pos[0]

            if tuple(tail_pos) not in tail_positions:
                tail_positions.append(tuple(tail_pos))

    print(tail_positions)
    print(len(tail_positions))

    # PART 2
    head_pos = [0, 0]
    tails = []
    tail_positions = [(0, 0)]

    # Initialize tails
    for index in range(9):
        tails.append([0,0])


    for index_2 in range(len(lines)):

        line = lines[index_2]
        # Split the line to get the full instruction
        line_split = line.split(' ')
        direction = line_split[0]
        number = int(line_split[1])

        for execution in range(number):
            head_pos = update_pos(head_pos, direction)

            # Update all the tails based on the head movement
            for index_3 in range(len(tails)):

                if index_3 == 0:
                    tails[index_3] = calc_tail(head_pos, tails[index_3])
                else:
                    tails[index_3] = calc_tail(tails[index_3-1], tails[index_3])

                # Add the final tail to the list of positions where the tail went
                if index_3 == len(tails)-1:
                    if tuple(tails[index_3]) not in tail_positions:
                        tail_positions.append(tuple(tails[index_3]))

    print(tail_positions)
    print(len(tail_positions))

def check_register_x(register_x, cycle_count, key_cycles, signal_strengths):
    '''
    Used by day 10. If the cycle count reaches one of the values in the key_cycles, then calculate the signal strength and append to
    the signal strengths list which you then return
    '''

    for number in key_cycles:
        if cycle_count == number:
            signal_strength = cycle_count * register_x
            signal_strengths.append(signal_strength)
            return signal_strengths

    return signal_strengths

def new_cycle(crt_pos, cycle_count, register_x, key_cycles):
    '''
    Used by day 10 part 2. Does a lot of checks depending on the new cycle.
    :return:
    '''

    cycle_count += 1
    crt_pos += 1

    # Check if we have reached a new line for the crt
    for number in key_cycles:
        if cycle_count == number:
            crt_pos = 0
            print(' ')

    # Evaluate what we should print based on the position of register x
    if crt_pos == register_x or crt_pos == register_x - 1 or crt_pos == register_x + 1:
        print('#', end='')
    else:
        print('.', end='')

    return crt_pos, cycle_count

def cathode_ray_tube():
    '''
    Day 10 - there are cycle instructions, use it to count some numbers in the first part and print letters in the
    second.
    '''

    cycle_instructions = os.getcwd() + '\input_day10.txt'
    lines = text_file_to_lines(cycle_instructions)

    cycle_count = 0
    register_x = 1
    key_cycles = [20, 60, 100, 140, 180, 220]
    signal_strengths = []

    for index in range(len(lines)):

        line = lines[index]

        if line.find('noop') != -1:
            cycle_count += 1
            signal_strengths = check_register_x(register_x, cycle_count, key_cycles, signal_strengths)
        elif line.find('addx') != -1:
            num_to_add = int(line.split(' ')[-1])

            cycle_count += 1
            signal_strengths = check_register_x(register_x, cycle_count, key_cycles, signal_strengths)
            cycle_count += 1
            signal_strengths = check_register_x(register_x, cycle_count, key_cycles, signal_strengths)
            register_x += num_to_add

    print(signal_strengths)
    print(sum(signal_strengths))

    # PART 2

    register_x = 1
    key_cycles = [1, 41, 81, 121, 161, 201]
    cycle_count = 0
    crt_pos = 0

    # Evaluate all the lines in the file to print the correct stuff.
    for index_2 in range(len(lines)):
        line = lines[index_2]

        if line.find('noop') != -1:
            crt_pos, cycle_count = new_cycle(crt_pos, cycle_count, register_x, key_cycles)
        if line.find('addx') != -1:
            num_to_add = int(line.split(' ')[-1])
            crt_pos, cycle_count = new_cycle(crt_pos, cycle_count, register_x, key_cycles)
            crt_pos, cycle_count = new_cycle(crt_pos, cycle_count, register_x, key_cycles)
            register_x += num_to_add

def monkey_in_the_middle():

    cycle_instructions = os.getcwd() + '\input_day11.txt'
    lines = text_file_to_lines(cycle_instructions)

monkey_in_the_middle()