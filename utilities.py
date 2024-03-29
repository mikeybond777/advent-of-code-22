def where_found_max(num, array):
    '''
    Returns the first index in the array where the num is not greater than list element.
    '''

    for index in range(len(array)):
        num_to_compare = array[index]

        if not num > num_to_compare:
            return index

    return len(array) - 1

def trim_last_char(string):
    '''
    Trim the last character in the string and return the new string.
    '''

    new_string = ''

    for i in range(len(string) - 1):
        new_string += string[i]

    return new_string

def get_above_directory(path):
    '''
    Takes a path and returns the string with the directory above (path should be in '/' form and not end with '/'.
    '''

    split_path = path.split('/')
    new_path = '/'

    for index in range(len(split_path) -2):
        new_path += split_path[index+1] + '/'

    # Trim off the last '/'
    new_path = trim_last_char(new_path)

    if new_path == '':
        new_path = '/'

    return new_path


def unique_string(string, num):
    '''
    Returns first num unique characters in the string provided and where this string starts.
    '''

    print(string, num)

    for index in range(num, len(string), 1):

        string_to_analyse = string[index-num:index]
        length_string = len(string_to_analyse)
        continue_loop = False

        # Search each character in the string (starting at the end), if the index where it is found is not where we
        # expect, then there is more than one and we should continue searching.
        for index_2 in range(length_string):
            index_3 = length_string-index_2-1
            character = string_to_analyse[index_3]
            if string_to_analyse.find(character) != index_3:
                continue_loop = True
                break

        if continue_loop:
            continue
        else:
            return string_to_analyse, index

    return None


def compare_lists(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))


def range_to_list(str_range):
    '''
    Converts a range of 4-7 into list [4,5,6,7] for example
    :return:
    '''

    list = []

    nums = str_range.split('-')

    first_num = int(nums[0])
    second_num = int(nums[1])

    for num in range(first_num, second_num+1, 1):
        list.append(num)

    return list

def split_list(list, index):
    '''
    Split a list in two based on the index provided.
    '''

    return list[:index], list[index:]

def calculate_rock_paper_scissors_score(p2_choice, outcome):
    '''
    Calculates the score from a game.
    :param p2_choice: Player 2 choice.
    :param outcome: Game outcome.
    :return:
    '''

    round_score = 0

    # Add score for the choice
    if p2_choice == 'ROCK':
        round_score += 1
    elif p2_choice == 'PAPER':
        round_score += 2
    elif p2_choice == 'SCISSORS':
        round_score += 3

    # Add score for the outcome
    if outcome == 'DRAW':
        round_score += 3
    elif outcome == 'PLAYER1':
        round_score += 0
    elif outcome == 'PLAYER2':
        round_score += 6

    return round_score


def rock_paper_scissors(p1_choice, p2_choice):
    '''
    Return the outcome of the game based on the choice of the two players.
    '''

    if p1_choice == p2_choice:
        return 'DRAW'
    elif p1_choice == 'ROCK':
        if p2_choice == 'SCISSORS':
            return 'PLAYER1'
        else:
            return 'PLAYER2'
    elif p1_choice == 'PAPER':
        if p2_choice == 'ROCK':
            return 'PLAYER1'
        else:
            return 'PLAYER2'
    elif p1_choice == 'SCISSORS':
        if p2_choice == 'PAPER':
            return 'PLAYER1'
        else:
            return 'PLAYER2'

def calculate_p2_choice(p1_choice, outcome):
    '''
    Calculate the player 2 choice from player 1 and the outcome (winner).
    '''

    if outcome == 'DRAW':
        return p1_choice
    if outcome == 'PLAYER2':
        if p1_choice == 'ROCK':
            return 'PAPER'
        if p1_choice == 'PAPER':
            return 'SCISSORS'
        if p1_choice == 'SCISSORS':
            return 'ROCK'
    if outcome == 'PLAYER1':
        if p1_choice == 'ROCK':
            return 'SCISSORS'
        if p1_choice == 'PAPER':
            return 'ROCK'
        if p1_choice == 'SCISSORS':
            return 'PAPER'


def swap_dict_keys_values(dictionary):
    '''
    Swap the values and keys in the dictionary (only works when there is one value per key.)
    :param dictionary: The dictionary to swap round.
    :return:
    '''

    return dict([(value, key) for key, value in dictionary.items()])

def text_file_to_lines(path):
    lines = []

    with open(path, 'r') as in_file:
        lines = [line.rstrip() for line in in_file]
        return lines

def swap_dict_pos(dictionary, pos_1, pos_2):
    '''
    Swaps two elements in a dictionary.
    :param dictionary: Dictionary we are going to be swapping items in.
    :param pos_1: Index of first item to swap.
    :param pos_2: Index of second item to swap.
    :return:
    '''

    # conversion to tuples
    tups = list(dictionary.items())

    # swapping by indices
    tups[pos_1], tups[pos_2] = tups[pos_2], tups[pos_1]

    # converting back
    dictionary = dict(tups)

    return dictionary

def bubble_sort_dict(dictionary):
    '''
    Bubble sorts a dictionary with string keys and numberic values by the number the of the values.
    :param dictionary: Dictionary to bubble sort
    :return:
    '''

    dict_values = list(dictionary.values())

    swapped = True

    while swapped == True:
        swapped = False

        for current_index in range(len(dict_values)-1):
            pos_1 = current_index
            pos_2 = current_index + 1

            if dict_values[pos_1] < dict_values[pos_2]:
                dictionary = swap_dict_pos(dictionary, pos_1, pos_2)
                swapped = True

    return dictionary


def get_key_from_value(dictionary, value):
    '''
    Get the key from the value.
    :param dictionary:
    :return:
    '''

    return list(dictionary.keys())[list(dictionary.values()).index(value)]

def sum_of_list(list):

    sum = 0

    for current_index in range(len(list)):
        sum += list[current_index]

    return sum