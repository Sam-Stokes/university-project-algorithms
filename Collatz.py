# Author : Sam Stokes
# Date : November 2020
"""
This program tests Collatz Conjecture for a given integer.
"""
import time


# The function starts with a number n > 1. If n is even, n is divided by 2.
# If n is odd, n is multiplied by 3 and 1 is added. This is repeated until n becomes 1.
def collatz(n):
    inp = n  # Original input number for print
    count = 0  # Variable to keep track of steps taken

    while n > 1:
        print('Step ', count + 1, ':', n)
        count = int(count + 1)
        if n % 2 == 0:  # n is even
            n = int(n / 2)
        else:  # n is odd
            n = int(3 * n + 1)
    else:
        count = int(count + 1)
        print('Step ', count, ':', n)
        print('')

    print('The number of steps to reach 1 from ', inp, ' is ', count)


def main():
    n = int(input('Input an integer: '))  # User input for the number to be tested
    start_time = time.perf_counter()
    collatz(n)  # Calls the above function
    end_time = time.perf_counter()
    print('Run time test case: ', (end_time - start_time))  # Run time test cases


main()  # Run program
