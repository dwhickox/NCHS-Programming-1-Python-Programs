"""
#David Hickox
#April 24 17
#GPA
#this will preform a variety of administrative functions
#variables
#   X, check varible
#   SELECT, the users choice
"""
import os

X == 0
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
while X == 0:
    SELECT = 0
    print("""
    Options are:
    1. School List
    2. Sophmores
    3. Juniors
    4. Above Average Students
    5. Alphabetical list
    6. Highest and Lowest GPA
    7. Find Student
    8. Exit
    """)
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
input("\nPress Enter to exit")

#1&
def schlist(z):
    print("Last\tFirst\tGrade\tSex\tGPA")
    if z == 0:
        for i in students:
            a, b, c, d, e = i
            print(a, b, c, d, e, sep = "\t")
    else:
        stusort = students.sort()
        for i in stusort:
            a, b, c, d, e = i
            print(a, b, c, d, e, sep = "\t")
#2&3
def junsoph(g):
    print("Last\tFirst\tGrade\tSex\tGPA")
    for i in students:
        if i[2] == g:
            a, b, c, d, e = i
            print(a, b, c, d, e, sep = "\t")
#4
def abovave():
    print("Last\tFirst\tGrade\tSex\tGPA")
    TOT = sum(ROW[4] for ROW in students)
    AVE = TOT/len(students)
    for i in students:
        if i[4] > AVE:
            a, b, c, d, e = i
            print(a, b, c, d, e, sep = "\t")
#5
def highlow():

def exitprgm():
    X = 1
