def print_phrases():
    """Print Monty-Python phrases to the console"""
    phrases = [
        "Nobody expects the Spanish Inquisition!",
        "'Tis but a scratch!",
        "And now for something completely different...",
        "My hovercraft is full of eels",
        "I fart in your general direction!",
        "She's got huge... tracts of land"
    ]

    for phrase in phrases:
        print(phrase)


def print_users():
    """Print user dictionary to the console, before and after manipulation by a for loop"""
    users = {
        "gchapman": "inactive",
        "jcleese": "active",
        "tgilliam": "active",
        "eidle": "active",
        "tjones": "inactive",
        "mpalin": "active"
    }

    # initial implementation of concatenation in print function:
    # print("BEFORE: " + users.__str__())
    # but Python can do this - and it reads much better
    print("BEFORE: ", users)

    # copy the dictionary for iteration, but make changes to the original
    for user, status in users.copy().items():
        if status == "inactive":
            del users[user]

    print("AFTER: ", users)


print_phrases()
print_users()
