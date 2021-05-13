# it's also possible to use separate import statements
import lists, insulter

if __name__ == "__main__":
    """Show how to use imported modules"""
    random_ints_list = lists.random_positive_ints(10, 100)
    print(random_ints_list)

    insult = insulter.insult_me()
    print(insult)
