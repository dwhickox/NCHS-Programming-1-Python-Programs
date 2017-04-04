"""
#David Hickox
#April 4 17
#Project 2
#This will display a user inputed message backwards
#variables
#   message, the message
"""
#prints welcome and has users input a message
print("Welcome to the Backwards program")
MESSAGE = input("\nPlease enter your message ")
print("\nYour message backwards is:", end=" ")
#flips and prints the message
for i in range(len(MESSAGE)):
    print(MESSAGE[-(i+1)], end="")

input("\n\nPress enter to exit!")
