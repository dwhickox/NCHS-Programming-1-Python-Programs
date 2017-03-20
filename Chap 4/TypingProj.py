"""
#David Hickox
#Mar 20 17
#Typing Program
#this will tell each of the 7 dwarfs if they can type fast enough or not
#variables
#   STUDENTS = names of the dwarfs
"""
STUDENTS = ["Bashful", "Doc", "Dopey", "Happy", "Sleepy", "Sneezy", "Grumpy"]

print ("Welcome to the Typing program")

for i in range(len(STUDENTS)):
    num = float(input("How many words per minute can "+STUDENTS[i]+" type? "))
    if num >= 150:
        print(STUDENTS[i].upper(),"PUT DOWN THE COFFEE!!!")
    elif num >= 25:
        print(STUDENTS[i],"you can type fast enough to pass Keyboarding")
    else:
        print(STUDENTS[i]+", sorry you need to type faster!")
input("Press Enter to exit")
