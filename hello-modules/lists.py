import random


def random_positive_ints(size, maximum):
    """
    Generate a list of random unsorted positive integers.

    :param size: the number of unsorted positive integers to return
    :param maximum: the upper-limit of positive integers to generate
    :return: a list of random unsorted positive integers
    """
    ints = []
    for i in range(0, size):
        ints.append(random.randint(0, maximum))
    return ints
