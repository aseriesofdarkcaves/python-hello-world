import random


def random_positive_ints(size, max):
    array = []
    for i in range(0, size):
        array.append(random.randint(0, max))
    return array
