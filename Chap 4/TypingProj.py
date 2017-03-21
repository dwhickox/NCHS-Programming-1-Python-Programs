"""
#David Hickox
#Mar 20 17
#Typing Program
#this will tell each of the 7 dwarfs if they can type fast enough or not
#variables
#   STUDENTS = names of the dwarfs
#   num = WPM
"""
STUDENTS = ["Bashful", "Doc", "Dopey", "Happy", "Sleepy", "Sneezy", "Grumpy"]

print("Welcome to the Typing program")
#starts the loop
for i in enumerate(STUDENTS):
    #asks for input
    num = float(input("How many words per minute can "+i[1]+" type? "))
    #checks to see what wpm someone types at
    if num >= 150:
        print(i[1].upper(), "PUT DOWN THE COFFEE!!!")
    elif num >= 25:
        print(i[1], "you can type fast enough to pass Keyboarding")
    else:
        print(i[1]+", sorry you need to type faster!")
input("Press Enter to exit")
