"""
#David Hickox
#April 24 17
#GPA
#this will preform a variety of administrative functions
#variables
#   X, check varible
#   SELECT, the users choice
#   single letter variables, temp placeholders for student info or function selectors
#   TOT = total gpa
#   AVE = average gpa
#   Stusort = sorted students list
"""
import os

#1&5
def schlist(z):
    print("Last\t\tFirst\t\tGrade\tSex\tGPA")
    if z == 0:
        for i in students:
            a, b, c, d, e = i
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
                print(a+'\t', b+'\t', c, d, e, sep="\t")
    else:
        stusort = students[:]
        stusort.sort()
        for i in stusort:
            a, b, c, d, e = i
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
                print(a+'\t', b+'\t', c, d, e, sep="\t")
#2&3
def junsoph(g):
    print("Last\t\tFirst\t\tGrade\tSex\tGPA")
    for i in students:
        if i[2] == g:
            a, b, c, d, e = i
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
                print(a+'\t', b+'\t', c, d, e, sep="\t")
#4
def abovave():
    print("Last\t\tFirst\t\tGrade\tSex\tGPA")
    TOT = sum(ROW[4] for ROW in students)
    AVE = TOT/len(students)
    for i in students:
        if i[4] > AVE:
            a, b, c, d, e = i
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
                print(a+'\t', b+'\t', c, d, e, sep="\t")
#5
def highlow():
    high = 2
    low = 2
    for i in students:
        if i[4] > high:
            high = i[4]
        if i[4] < low:
            low = i[4]
    for i in students:
        if i[4] == high:
            a, b, c, d, e = i
            print("The highest gpa in the class is:")
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
                print(a+'\t', b+'\t', c, d, e, sep="\t")
    for i in students:
        if i[4] == low:
            a, b, c, d, e = i
            print("The lowest gpa in the class is:")
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
                print(a+'\t', b+'\t', c, d, e, sep="\t")
#6
def findstu():
    found = 0
    print("Which student would you like to find?")
    stufind = input("Please enter only a last name: ")
    for i in students:
        if i[0] == stufind.title():
            a, b, c, d, e = i
            if len(a) > 7 and len(b) > 7:     
                print(a, b, c, d, e, sep="\t") 
            elif len(a) > 7:
                print(a, b+"\t", c, d, e, sep="\t") 
            elif len(b) > 7:
                print(a+"\t", b, c, d, e, sep="\t")
            else:
              print(a+'\t', b+'\t', c, d, e, sep="\t")
            found = 1
    if found == 0:
        print("Student not found")
        found = 0

#these values are chosen simply because there is a gpa both above and below 2
high = 2
low = 2
#sets up the rest of the variables
X = 0
found = 0
z = 0
# nested sequence of students first name, last name, year, gender, and gpa
students = [["White", "Snow", 9, "F", 3.56],
            ["Sprat", "Jack", 12, "M", 2.0],
            ["Contrary", "Mary", 9, "F", 3.674],
            ["Dumpty", "Humpty", 11, "M", 2.342],
            ["Bunny", "Easter", 10, "M", 4.233],
            ["Wonderland", "Alice", 10, "F", 3.755],
            ["Bunyon", "Paul", 11, "M", 1.434],
            ["Penny", "Henny", 9, "F", 2.54],
            ["Hatter", "Mad", 11, "M", 4.522],
            ["Munk", "Chip", 10, "M", 3.0],
            ["Hood", "Red Riding", 10, "F", 3.137],
            ["Bunny", "Bugs", 11, "M", 2.12],
            ["Duck", "Daffy", 11, "M", 3.564],
            ["Ant", "Atom", 12, "M", 3.333],
            ["Mouse", "Mickey", 10, "M", 3.975],
            ["Brown", "Charlie", 9, "M", 1.25]]
print("Welcome to the GPA program")
#while loop runs whole program and calls the correct function based on what it wants to do
while X == 0:
    #resets all the variables used in the program just incase something is rerun and not correct.
    SELECT = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    i = 0
    z = 0
    found = 0
    TOT = 0
    AVE = 0
    high = 2
    low = 2
    #creates menu
    print("""
    Your administrative options are:
    1. School List
    2. Sophmores
    3. Juniors
    4. Above Average Students
    5. Alphabetical list
    6. Highest and Lowest GPA
    7. Find Student
    8. Exit
    """)
    #asks the user for in
    SELECT = int(input("Which would you like to do (please enter a number)? "))
    os.system('cls') #clears screen
    if SELECT == 1:
        schlist(0)
    elif SELECT == 2:
        junsoph(10)
    elif SELECT == 3:
        junsoph(11)
    elif SELECT == 4:
        abovave()
    elif SELECT == 5:
        schlist(1)
    elif SELECT == 6:
        highlow()
    elif SELECT == 7:
        findstu()
    elif SELECT == 8:
        X = 1
    else:
        print("That is not an option please try again!")
