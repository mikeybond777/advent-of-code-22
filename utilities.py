def rock_paper_scissors(p1_choice, p2_choice):

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