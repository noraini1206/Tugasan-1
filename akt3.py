import random

def main():
    """start a number guessing game between 1 - 50."""
    print("Guess the number!")
    x = random.randint(1, 50)
    x = random.randint(1, 50)
    guess = None

    while x != guess:

        guess=int(input("pick a number between 1 to 50:" ))

        if x == guess :
            print("You Genius!")
        else: #x > guess:
            print("wrong answer.")
           # break
        #elif x < guess:
             #print ("Try a Smaller number.")
main()