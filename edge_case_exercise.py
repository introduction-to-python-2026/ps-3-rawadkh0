def move(my_list, direction):
    # Make a copy so we don't modify the original list
    new_list = my_list.copy()

    # Find the index of the 1
    index_of_one = new_list.index(1)

    # Move right
    if direction == "right":
        if index_of_one == len(new_list) - 1:
            return new_list      # at right edge, do nothing
        new_list[index_of_one] = 0
        new_list[index_of_one + 1] = 1

    # Move left
    elif direction == "left":
        if index_of_one == 0:
            return new_list      # at left edge, do nothing
        new_list[index_of_one] = 0
        new_list[index_of_one - 1] = 1

    return new_list
