#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov. 16th, 2022
# This program gets an integer from the user
# and displays the multiplication table from numbers 0 - 10


def main():

    import math

    # Initializing the counter and number
    numbers = 0

    user_input_as_string = input("What multiplication table do you want to see? ")

    try:
        # Making the user input an integer
        user_input = int(user_input_as_string)

        # If the numbers are below 11 the loop will run
        while numbers < 11:
            # if the user input is below zero
            if user_input < 0:
                print("please enter a positive integer")
                # Stops the loop
                break
            # Multiplying the user input by the numbers counter
            answer = numbers * user_input
            # Printing the multiplication table
            print("{} x {} = {}".format(numbers, user_input, answer))
            numbers = numbers + 1

    except ValueError:
        print("Please input a number")


if __name__ == "__main__":
    main()
