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
    """
    Generate a list of random unsorted positive integers in the range 0-1000.

    :param size: the number of unsorted positive integers to return
    :return: a list of randomised positive integers with the given size
    """
    randomised_ints = []
    for integers in range(0, size):
        randomised_ints.append(random.randint(0, 1000))
    return randomised_ints


def get_unsorted_lists():
    """
    Setup the values to be used during the benchmarking process.

    :return: a list of lists with unsorted random positive integers
    """
    # TODO: consider using tuples instead of lists if they contain static values
    list_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    unsorted_lists = []
    for size in list_sizes:
        unsorted_lists.append(get_randomised_ints(size))
    return unsorted_lists


if __name__ == "__main__":
    """Do the benchmarking of the sorting algorithms"""
    # TODO: figure out a way to iterate over the algorithms
    #   something like the strategy/command pattern?
    #   create various objects that are configured with the different sorting algorithms as a field
    #   field could be an interface called sortable which has a sort function (but the python equivalent)
    #   add these objects to a list
    #   iterate over the list, calling object.sort each time
    #   Update:
    #   This may be easier in python becuase of first-class functions
    averaged_results = {}

    for unsorted_list in get_unsorted_lists():
        single_cumulative_result = 0
        print("Running bubblesort for list of size:", len(unsorted_list))
        for i in range(0, 10):
            start_time = time.time()
            bubblesort(unsorted_list)
            end_time = time.time()
            elapsed_time = end_time - start_time
            single_cumulative_result += elapsed_time
            # TODO: PyCharm console doesn't seem to want to print the dots individually, only on a newline,
            #  despite having set the flush keyword arg to True, what's up with that?
            if i < 9:
                print(".", end="", flush=True)
            else:
                print(".")
        averaged_results[len(unsorted_list)] = round((single_cumulative_result / 10), 3)

    print("Averages:", averaged_results)
