#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    try:
        value = int(sys.argv[1])
        f = factorial(value)
        print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")
else:
    print("Usage: ./factorial.py <number>")
