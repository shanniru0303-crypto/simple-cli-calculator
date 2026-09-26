"""
Simple CLI Calculator
Version: 1.0.0

Supports: addition, subtraction, multiplication, division,
power, and square root.
"""

import math

VERSION = "1.1.0"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # FIXED in 1.1.0: division by zero now returns a friendly error
    # message instead of raising ZeroDivisionError and crashing.
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    # FIXED in 1.1.0: negative input now returns a friendly error
    # message instead of raising ValueError and crashing.
    if a < 0:
        return "Error: Cannot compute square root of a negative number"
    return math.sqrt(a)


MENU = """
==== Simple Calculator (v{version}) ====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power (a ^ b)
6. Square Root
7. Exit
=======================================
"""


def get_number(prompt):
    value = input(prompt)
    return float(value)


def main():
    while True:
        print(MENU.format(version=VERSION))
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        try:
            if choice in ("1", "2", "3", "4", "5"):
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
            elif choice == "6":
                a = get_number("Enter a number: ")
            else:
                print("Invalid option. Please choose 1-7.")
                continue

            if choice == "1":
                print(f"Result: {add(a, b)}")
            elif choice == "2":
                print(f"Result: {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {multiply(a, b)}")
            elif choice == "4":
                print(f"Result: {divide(a, b)}")
            elif choice == "5":
                print(f"Result: {power(a, b)}")
            elif choice == "6":
                print(f"Result: {square_root(a)}")

        except ValueError:
            print("Error: Please enter valid numeric input.")


if __name__ == "__main__":
    main()
