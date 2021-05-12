import lists
import insulter

if __name__ == "__main__":
    random_ints_list = lists.random_positive_ints(10, 100)
    print(random_ints_list)

    insult = insulter.insult_me()
    print(insult)
