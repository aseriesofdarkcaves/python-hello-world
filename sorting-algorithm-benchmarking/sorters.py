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


def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heapsort(numbers):
    """
    Heap sort algorithm, nicked from:
    https://stackabuse.com/sorting-algorithms-in-python/

    :param numbers: the list of integers to be sorted
    :return: the sorted list
    """
    n = len(numbers)
    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(numbers, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def mergesort(numbers):
    """
    Merge sort algorithm, nicked from:
    https://stackabuse.com/sorting-algorithms-in-python/
    
    :param numbers: the list of integers to be sorted
    :return: the sorted list
    """
    # If the list is a single element, return it
    if len(numbers) <= 1:
        return numbers

    # Use floor division to get midpoint, indices must be integers
    mid = len(numbers) // 2

    # Sort and merge each half
    left_list = mergesort(numbers[:mid])
    right_list = mergesort(numbers[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quicksort(numbers):
    """
    Quick sort algorithm, nicked from:
    https://stackabuse.com/sorting-algorithms-in-python/
    
    :param numbers: the list of integers to be sorted
    :return: the sorted list
    """

    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(numbers, 0, len(numbers) - 1)
