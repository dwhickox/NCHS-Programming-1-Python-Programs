#David Hickox
#Mar 10 17
#Name program
#gives you stats about your name
#variables
#   i = tells the program which name it should append letters to
#   first = first name
#   middle = middle name
#   last = last name
#   check = tells the program whether or not you have a z in your name
#   nxtletter = tells the program if the next letter should be the start to a new word
#   cont = tells the program if a word is still continuous, aka the program has not hit another space after the word started
#   spaces = counts how many spaces there are to count the number of words (spaces as in space between words, 3 space bar hits is still just one "space")
#   spacebar = total space bar hits
#   name = users name 


print("Welcome to the Name Program\n")
i = 1
first = ""
middle = ""
last = ""
check = "f"
nxtletter = "f"
cont = "f"
initials = ""
count = 0
spaces = 0
spacebar = 0
name = input("What is your name? ")
print("The lenght of your name with spaces is", len(name), "characters")
for letter in name:
    #this checks to see if there is a z in the name
    
    if letter.lower() == "z":
        check = "t"
    #checks to see if the letter is a space, since the next letter should be an inital 
    if letter.lower() == " " and nxtletter != "t":
        nxtletter = "t"
        i+=1
        spaces += 1
    if letter.lower() == " ":
        spacebar += 1
    #checks to see if the letter previous was a space and the current letter is not a space indicating that the current letter would be an intial
    if ((nxtletter == "t" or cont == "t") and letter.lower() != " ")or count == 0:
        if i == 1:
            first += letter
        elif i == 2:
            middle += letter
        elif i == 3:
            last += letter
        else:
            print("no if triggered")
        cont = "t"
    else:
        cont = "f"
    if (nxtletter == "t" and letter.lower() != " ") or count == 0:
        initials += letter.upper()
        nxtletter = "f"
    count +=1

print("The lenght of your name without spaces is", len(name)-spacebar, "characters")        
if check == "t":
    print("You have a unique name!")
else:
    print("Your name doesn't include a Z")
if spaces > 0:
    print("Your initials are",initials)
if spaces == 2:
    print("First name =",first.title())
    print("Middle name =",middle.title())
    print("Last name =",last.title())
elif spaces == 1:
    print("First name =",first.title())
    print("Last name =",middle.title())
else:
    print("First name =",first.title())


input("\nPress Enter to Exit")
