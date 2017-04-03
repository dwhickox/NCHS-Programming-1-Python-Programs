"""
#David Hickox
#Mar 24 17
#Blackjack Program
#This will play a handycaped version of Blackjack
#variables
#   array = an array with human cards in column 0 and computer
#       cards in column 1, winnings in column 2
#   i = sentry
#   card = number of cards the human wants
"""
import random
#initializes the array hight and with variables
H = 4
W = 3
#initialises the array
ARRAY = [[0 for Y in range(H)] for X in range(W)]
print("Welcome to the Blackjack program")
#sets up sentry
I = "y"
#handels all of the repeating logic
while I.lower() == 'y' or I.lower() == 'yes':
    #resets card totals
    ARRAY[0][3] = 0
    ARRAY[1][3] = 0
    #asks the user how many cards they want
    CARD = int(input("How many cards do you want? "))
    while CARD > 3:
        CARD = int(input("You cannot choose more than 3 cards! How many cards do you want? "))
    #Picks cards for user
    for i in range(CARD):
        ARRAY[0][i] = random.randrange(1, 11)
        ARRAY[0][3] += ARRAY[0][i]
    #prints user cards
    print("You:", ARRAY[0][0], ARRAY[0][1], ARRAY[0][2], sep="\t")
    # checks to see if the user busts
    if ARRAY[0][3] > 21:
        print("Sorry you bust!")
        ARRAY[2][0] += 1
    else:
        #assigns computer cards
        for i in range(3):
            ARRAY[1][i] = random.randrange(1, 11)
            ARRAY[1][3] += ARRAY[1][i]
        #displayes computer cards
        print("Me:", ARRAY[1][0], ARRAY[1][1], ARRAY[1][2], sep="\t")
        #checks to see who won
        if ARRAY[1][3] > 21:
            print("I bust and you win!")
            ARRAY[2][1] += 1
        elif ARRAY[0][3] > ARRAY[1][3]:
            print("I have", ARRAY[1][3], "and you have", ARRAY[0][3], "so you win!")
            ARRAY[2][1] += 1
        elif ARRAY[0][3] < ARRAY[1][3]:
            print("I have", ARRAY[1][3], "and you have", ARRAY[0][3], "so I win!")
            ARRAY[2][0] += 1
        else:
            print("I have", ARRAY[1][3], "and you have", ARRAY[0][3], "so we tie!")
            ARRAY[2][2] += 1
    #asks the user if s/he wishes to play again 
    I = input("Would you like to continue? (Y/N) ")
#Prints the results 
print("My Winnings =", ARRAY[2][0])
print("Your Winnings =", ARRAY[2][1])
print("Draws =", ARRAY[2][2])
input('Press Enter to Exit!')
