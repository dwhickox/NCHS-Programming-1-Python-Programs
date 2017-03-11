#David Hickox
#Mar 11 17
#Name slice prgm
#variables
#   name = my name

print("Welcome to the name program")
name = "David William Hickox"
if "z" in name:
    print("You have a unique name")
else:
    print('You do not have a z in your name')

print("Intials =\t"+name[0]+name[6]+name[14])
print("First name:\t"+name[:5])
print("Last name:\t"+name[6:13])
print("Last name:\t"+name[14:])

input("Press enter to exit.")
