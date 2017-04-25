"""
#David Hickox
#April 24 17
#GPA
#this will preform a variety of administrative functions
#variables
#   X, check varible
#   SELECT, the users choice
"""
X == 0
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
input("\nPress Enter to exit")


def exitprgm():
    X = 1
