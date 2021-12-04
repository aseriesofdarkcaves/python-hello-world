import random

insults = [
    "You don't frighten us, English pig-dogs!",
    "Go and boil your bottoms, son of a silly person!",
    "I blow my nose at you!",
    "I don't want to talk to you no more, you empty-headed, animal food-trough wiper!",
    "I fart in your general direction!",
    "Your mother was a hamster and your father smelt of elderberries!",
    "Now go away, or I shall taunt you a second time!"
]


def insult_me():
    """
    Insults you. You have been warned.

    :return: a random insult string
    """
    list_size = len(insults)
    # produces an integer N, where a <= N <= b
    random_index = random.randint(0, list_size - 1)
    return insults[random_index]
