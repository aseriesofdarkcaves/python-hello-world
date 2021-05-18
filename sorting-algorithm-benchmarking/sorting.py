def bubblesort(integer_list):
    """
    Bubblesort sorting algorithm, stolen from:
    https://github.com/AtomsForPeace/reinventing-the-wheel/blob/master/bubble_sort.py

    :param integer_list: list of integers to be sorted
    :return: the sorted list
    """
    unsorted = []
    while True:
        if len(unsorted) + 1 == len(integer_list):
            break
        unsorted = []
        for index, i in enumerate(integer_list[:-1]):
            if integer_list[index] > integer_list[index + 1]:
                move_forward = integer_list[index + 1]
                del integer_list[index + 1]
                integer_list.insert(move_forward, index)
            else:
                unsorted.append(True)
    return integer_list
