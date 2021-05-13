def bubblesort(integer_list):
    """
    Return a sorted version of the input list.
    I didn't write this - it was stolen from the Internet!
    """
    size = len(integer_list)
    for i in range(size):
        complete_sort = True
        for j in range(size - i - 1):
            if integer_list[j] > integer_list[j + 1]:
                integer_list[j], integer_list[j + 1] = integer_list[j + 1], integer_list[j]
                complete_sort = False
        if complete_sort:
            break
    return integer_list
