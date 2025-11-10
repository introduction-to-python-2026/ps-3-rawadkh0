def move(my_list, direction):
    # מצא את מיקום ה-1
    idx = my_list.index(1)
    n = len(my_list)

    # עותק כדי לא לשנות את הקלט
    res = my_list[:]  

    if direction == 'right' and idx < n - 1:
        res[idx], res[idx + 1] = 0, 1
    elif direction == 'left' and idx > 0:
        res[idx], res[idx - 1] = 0, 1

    return res

