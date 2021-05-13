import random


def random_positive_ints(size, maximum):
    """Return a list of random unsorted positive integers"""
    ints = []
    for i in range(0, size):
        ints.append(random.randint(0, maximum))
    return ints
