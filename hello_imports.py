from time import sleep
import math

if __name__ == "__main__":
    """Demonstrate the use of imports"""
    # need to prefix the function with the module name here
    print("Factorial of 5 is:", math.factorial(5))

    sleep_time = 5
    print("Sleep time is set to", sleep_time, "seconds...")
    # don't need to prefix this function call with the module name here
    sleep(sleep_time)
    print("Finished sleeping!")
