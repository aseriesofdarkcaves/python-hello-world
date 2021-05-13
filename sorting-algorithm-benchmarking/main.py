"""
I think the goal here was to do something like this:
- Run a sorting algorithm on lists of ever increasing size, n
- Calculate the average time taken to sort each list of size n,
  meaning - run the algorithm x times and divide the cumulative result by x
- Do the same for various other algorithms
- Print the results
"""
import random
import time
from sorting import bubblesort


def get_randomised_ints(size):
    """Return a list of randomised positive integers with the given size"""
    integers = []
    for i in range(0, size):
        integers.append(random.randint(0, 1000))
    return integers


def get_unsorted_lists():
    """Return a list of lists with unsorted random positive integers"""
    list_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    unsorted_lists = []
    for size in list_sizes:
        unsorted_lists.append(get_randomised_ints(size))
    return unsorted_lists


if __name__ == "__main__":
    """Do the benchmarking of the sorting algorithms"""
    # use a dictionary with size as key?
    averaged_results = []
    # averaged_results = {}

    for unsorted_list in get_unsorted_lists():
        single_cumulative_result = 0
        for i in range(0, 10):
            start_time = time.time()
            bubblesort(unsorted_list)
            end_time = time.time()
            elapsed_time = end_time - start_time
            single_cumulative_result += elapsed_time
        averaged_results.append(round(single_cumulative_result / 10, 3))
        # averaged_results[len(unsorted_list)] = (single_cumulative_result / 10)

    for result in averaged_results:
        print(result)
