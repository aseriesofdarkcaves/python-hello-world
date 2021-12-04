"""
Adapted from: https://stackoverflow.com/a/8919545/4214228
"""


def strategy_add(a, b):
    """
    Strategy for adding two numbers.
    """
    return a + b


def strategy_minus(a, b):
    """
    Strategy for subtracting two numbers.
    """
    return a - b


solver = strategy_add
print(solver, ":", solver(1, 2))
solver = strategy_minus
print(solver, ":", solver(2, 1))
