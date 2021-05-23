def bubblesort(numbers):
    """
    Bubblesort sorting algorithm, stolen from:
    https://github.com/AtomsForPeace/reinventing-the-wheel/blob/master/bubble_sort.py

    :param numbers: the list of integers to be sorted
    :return: the sorted list
    """
    unsorted = []
    while True:
        if len(unsorted) + 1 == len(numbers):
            break
        unsorted = []
        for index, i in enumerate(numbers[:-1]):
            if numbers[index] > numbers[index + 1]:
                move_forward = numbers[index + 1]
                del numbers[index + 1]
                numbers.insert(move_forward, index)
            else:
                unsorted.append(True)
    return numbers


def selectionsort(numbers):
    """
    Selection sort algorithm, nicked from:
    https://stackabuse.com/sorting-algorithms-in-python/

    :param numbers: the list of integers to be sorted
    :return: the sorted list
    """
    # This value of i corresponds to how many values were sorted
    for i in range(len(numbers)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted element
        numbers[i], numbers[lowest_value_index] = numbers[lowest_value_index], numbers[i]


def insertionsort(numbers):
    """
    Insertion sort algorithm, nicked from:
    https://stackabuse.com/sorting-algorithms-in-python/

    :param numbers: the list of integers to be sorted
    :return: the sorted list
    """
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(numbers)):
        item_to_insert = numbers[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and numbers[j] > item_to_insert:
            numbers[j + 1] = numbers[j]
            j -= 1
        # Insert the item
        numbers[j + 1] = item_to_insert
