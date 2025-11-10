def move(my_list, direction):
    # Find the index of the '1'
    index_of_one = my_list.index(1)

    # Move right only if not at the right edge
    if direction == 'right' and index_of_one < len(my_list) - 1:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    # Move left only if not at the left edge
    elif direction == 'left' and index_of_one > 0:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    # If at an edge: do nothing
    return my_list

