import random

insult_count = 0

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
    insult_count = len(insults)
    random_index = random.randint(0, insult_count)
    return insults[random_index]
