"""
#David Hickox
#Mar 20 17
#games program
#this will organize a game night
#variables
#   GAMES = the games that are to be played
"""

print("Welcome to the Games program")
GAMES = []
i = 0
while i < 5:
    GAMES.append((input("What is game number "+str(i+1)+"? ")).title())
    i += 1
print("\n\nHere are the games that will be available tonight\n")
GAMES.sort()
for i in GAMES:
    print(i)

input("\n\nPress Enter to exit")
