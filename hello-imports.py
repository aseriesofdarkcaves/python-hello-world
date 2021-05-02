from time import sleep

if __name__ == "__main__":
    sleep_time = 5
    print("Sleep time is set to " + sleep_time.__str__() + " seconds...")
    sleep(sleep_time)
    print("Finished sleeping!")
