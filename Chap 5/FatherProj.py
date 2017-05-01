"""
#David Hickox
#April 30 17
#Proj 3
#this will find fathers and grandfathers
#variables
#   dictionary: the father son pairs
#   x: keeps the while loop working
#   son, son selection
#   father, father selection, or found fathers from dictionary
#   grandfather, grandfather found from father 
#   SELECT, the selection of option
"""
dictionary = {"Bart Simpson":"Homer Simpson", "Keifer Sutherland":"Donald Sutherland",
              "Luke Skywalker":"Darth Vader", "Ben Stiller":"Jerry Stiller",
              "Michael Douglas":"Kirk Douglas", "Charlie Sheen":"Martin Sheen",
              "Emilio Estevez":"Martin Sheen", "Homer Simpson":"Abraham Simpson",
              "Donald Sutherland":"Michael Ferrier", "Darth Vadar":"George Lucas",
              "Jerry Stiller":"William Stiller", "Kirk Douglas":"Harry Douglas",
              "Martin Sheen":"Francisco Estevez"}

print("Welcome to the Father Program")
x = 0
while x == 0:
    print("""
    Find a Son-Father:         1
    Add a Son-Father:          2
    Replace a Son-Father:      3
    Delete Son-Father:         4
    Find Grandson-Grandfather: 5
    Exit:                      6
    """)
    SELECT = int(input("Please select an option (enter a number): "))
    if SELECT == 1:
        son = (input("What is the sons name? ")).title()
        father = dictionary.get(son, "This is not a character")
        if father != "This is not a character":
            print("The father is:", father)
        else:
            print(father, "please try again!")
    elif SELECT == 2:
        son = (input("What is the sons name? ")).title()
        father = (input("What is the fathers name? ")).title()
        dictionary[son] = father
        print("added")
    elif SELECT == 3:
        son = (input("Which father son pair do you wish to replace? (enter the son's name) ")).title()
        if dictionary.get(son,1) == 1:
            print("This pair does not exist, please try again")
        else:
            del dictionary[son]
            son = (input("What is the new sons name? ")).title()
            father = (input("What is the new fathers name? ")).title()
            dictionary[son] = father
            print("Replaced")
    elif SELECT == 4:
        son = (input("Which father son pair do you wish to remove? (enter the son's name) ")).title()
        if dictionary.get(son,1) == 1:
            print("This pair does not exist, please try again")
        else:
            del dictionary[son]
            print("Removed")
    elif SELECT == 5:
        son = (input("What is the grandsons name? ")).title()
        if dictionary.get(son,1) == 1:
            print("This pair does not exist, please try again")
        else:
            father = dictionary.get(son)
            if dictionary.get(father,1) == 1:
                print("This person has a father in the system but no grandfather, please try again")
            else:
                grandfather = dictionary.get(father)
                print("The grandfather is:", grandfather)
    elif SELECT == 6:
        x = 1
    else:
        print("This is not an option please try again")
