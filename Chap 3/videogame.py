# Mrs. Epstein
# February 7, 2017
# Video Game Program
# This program will display an appropriate message depending on how many points
# a player earned on a video game.
# Variables:
#   points - the number of points earned by the player
#   message - the appropriate message depending on points

print ("Welcome to the Video Game Program\n")

# asks how many points were earned
points = float(input("What was your score?"))

# assigns an appropriate message depending on points earned
if points > 50000:
    message =  "You completed the highest level."
elif points > 35000:
    message =  "You completed level 2."
elif points > 20000:
    message =  "You completed level 1."
else:
    message =  "You should not play this game - you are terrible!"

# displays the appropriate message
print ("\nBased on your score of", points)
print (message)

input("\nPress enter to exit.")
