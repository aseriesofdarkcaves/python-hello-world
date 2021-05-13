import random


def random_positive_ints(size, max):
    """Return a list of random unsorted positive integers"""
    list = []
    for i in range(0, size):
        list.append(random.randint(0, max))
    return list
