# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random  # import random module

n = random.randrange(1, 100)     # select a random from 1 to 100

guess = int(input("Guess a number(1-100): "))  # Tell user to guess the number

while n != 0:
    if guess < n:
        print("Number is Too Low!")
        guess = int(input("Guess a number(1-100): "))
    elif guess > n:
        print("Number is Too High!")
        guess = int(input("Guess a number(1-100): "))
    else:
        break
print("You Guessed it right!")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
