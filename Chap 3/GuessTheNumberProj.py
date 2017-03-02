#David Hickox
#Mar 2 17
#Project 3
#guess the number program
#variables
#   num, the number to be guessed
#   guess, the guessed number
#   tries, the number of tries

#imports the the random package 
import random

print("Welcome to the Guess the number 1-100 Program\n")

num = random.randint(1,100)
tries = 1
guess = int(input("What is your guess? "))
while guess != num and tries < 5:
    if guess > num:
        print("\nWrong, Lower")
    else:
        print("\nWrong, Higher")
    guess = int(input("\nWhat is your guess? "))
    tries += 1
if guess == num:
    print("\nCongrats, you guessed the number!!!,",guess,"was correct!")
else:
    print("\nYou failed, and wasted your 5 tries, the number was ",num,".",sep="")

input("\nPress Enter to Exit")
