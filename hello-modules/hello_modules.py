# while it is possible to place imports on the same line, PEP standards recommend the following
import insulter
import lists

if __name__ == "__main__":
    """Show how to use imported modules"""
    random_ints_list = lists.random_positive_ints(10, 100)
    print(random_ints_list)

    insult = insulter.insult_me()
    print(insult)
