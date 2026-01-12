#!/usr/bin/python3
import sys

def factorial(n):
    """
    SECTION 1: Function Description
    Calculates the factorial of a given non-negative integer using recursion.
    The factorial of n (n!) is the product of all positive integers less than or equal to n.

    SECTION 2: Parameters
    n (int): The non-negative integer to calculate the factorial of.

    SECTION 3: Returns
    int: The factorial of the number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        # Recursive call: n * (n-1)!
        return n * factorial(n - 1)

# Execution block
if len(sys.argv) > 1:
    f = factorial(int(sys.argv[1]))
    print(f)
