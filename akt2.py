#!/usr/bin/env python

import random

def main():
    """start a number guessing game between 1 - 100."""
    print("Guess the number!")
    x = random.randint(1, 100)
    x = random.randint(1, 100)
    guess = None

    while x != guess:

        guess=int(input("pick a number between 1 to 100:" ))

        if x == guess :
            print("You Genius!")
        elif x > guess:
            print ("Try a bigger number.")
        elif x < guess:
             print ("Try a Smaller number.")
main()
