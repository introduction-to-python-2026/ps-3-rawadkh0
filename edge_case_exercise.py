def move(my_list, direction):
    # Find the index of the 1 in the list
    index_of_one = my_list.index(1)

    # If direction is right
    if direction == "right":
        # Edge case: already at the rightmost position
        if index_of_one == len(my_list) - 1:
            return my_list  # stay in place

        # Normal move
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    # If direction is left
    elif direction == "left":
        # Edge case: already at the leftmost position
        if index_of_one == 0:
            return my_list  # stay in place

        # Normal move
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
