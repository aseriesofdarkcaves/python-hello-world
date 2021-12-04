import random
import time
from sorters import bubblesort, insertionsort, selectionsort, heapsort, mergesort, quicksort


def get_sorting_algorithms():
    """
    Get all of the sorting algorithms under test.

    :return: a list of the sorting algorithm function-references
    """
    return (
        bubblesort,
        insertionsort,
        selectionsort,
        heapsort,
        mergesort,
        quicksort
    )


def get_unsorted_ints():
    """
    Setup the values to be used during the benchmarking process.

    :return: a list of lists with unsorted random positive integers
    """
    sizes = 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000
    # TODO: return a tuple here instead
    unsorted_ints = []
    for size in sizes:
        unsorted_ints.append(get_randomised_ints(size))
    return unsorted_ints


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


def main():
    """
    Benchmark the sorting algorithms.
    """
    results = {}

    for algorithm in get_sorting_algorithms():
        averaged_results = {}
        sorter = algorithm
        for unsorted_ints in get_unsorted_ints():
            single_cumulative_result = 0
            print("Running", sorter.__name__, "for list of size:", len(unsorted_ints))
            for i in range(0, 10):
                start_time = time.time()
                sorter(unsorted_ints)
                end_time = time.time()
                elapsed_time = end_time - start_time
                single_cumulative_result += elapsed_time
            averaged_results[len(unsorted_ints)] = round((single_cumulative_result / 10), 3)
        results[sorter.__name__] = averaged_results

    print(*results.items(), sep="\n")


if __name__ == "__main__":
    main()
