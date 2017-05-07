"""calculates the users weight on different plannets"""
#func def:
def menu():
    """creates the main menu"""
    #asks the user which planet they wish to know their weight on
    print("""
What celestial body do you want to know your weight on?
1. Venus
2. Moon
3. Mars
4. Jupiter""")
    planet = input("\nPlease enter your choice. ")
    #askes user to input their weight
    weight = float(input("What is your weight on earth? "))
    return planet, weight

def calc(temp):
    # this lets th functions be stacked
    planet, weight = temp
    """runs the calculation to find the final output"""
    #saves weight for later use sinve variable weight is changed
    orgwt = weight
    #else trigger for makeing the error look nice
    e = 0
    #does the math for weight on the correct planet
    if planet == "1" or planet.lower == "venus":
        weight = weight*.91
        planet = "Venus"
    elif planet == "2" or planet.lower == "moon":
        weight = weight*.17
        planet = "The Moon"
    elif planet == "3" or planet.lower == "mars":
        weight = weight*.38
        planet = "Mars"
    elif planet == "4" or planet.lower == "jupiter":
        weight = weight*2.54
        planet = "Jupiter"
    else:
        #changes e to say that the program needs to change the look of the output
        e = 1
        weight = "This was not an acceptable choice!"
    return weight, orgwt, e, planet

def printfunc(temp):
    """prints the final output"""
    # this lets th functions be stacked
    weight, orgwt, e, planet = temp
    #figures out which style output is required
    if e == 0:
        if len(planet) > 7:
            print("\nPlanet\t\tPlanet Weight")
            print("Earth", orgwt, sep="\t\t")
            print(planet, weight, sep="\t")
        else:    
            print("\nPlanet\tPlanet Weight")
            print("Earth", orgwt, sep="\t")
            print(planet, weight, sep="\t")
    else:
        print("\n", weight, sep="")
#main def:
def main():
    """the main function, runs the program"""
    printfunc(calc(menu()))




#David Hickox
#May 7 17
#Space weight
#calculates the users weight on different plannets
#variables
#   weight, weight of the user
#   planet, the planet selected by the user.
#   e, handles else
#   orgwt, stors the original weight on earth of the user
#functions:
#   menu, creates the menu
#   calc, does the weight calculation based upon which choice the user makes
#   printfunc, prints the end result

print("Welcome to the Celestial Weight Program\n")

main()

input("\nPress Enter to Exit")
