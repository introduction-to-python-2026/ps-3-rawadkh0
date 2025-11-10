def move(my_list, direction):
    # מצא את המיקום של ה־1
    i = my_list.index(1)

    if direction == 'right':
        # זזים ימינה רק אם לא בקצה הימני
        if i < len(my_list) - 1:
            my_list[i] = 0
            my_list[i + 1] = 1

    elif direction == 'left':
        # זזים שמאלה רק אם לא בקצה השמאלי
        if i > 0:
            my_list[i] = 0
            my_list[i - 1] = 1

    # אם היינו בקצה – נשארים במקום
    return my_list

