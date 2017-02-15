#David Hickox
#Feb 14 17
#Space weight
#calculates the users weight on different plannets
#variables
#   weight, weight of the user
#   planet, the planet selected by the user.
#   e, handles else
#   orgwt, stors the original weight on earth of the user

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Celestial Weight Program\n")

#askes user to input their weight
weight = float(input("What is your weight on earth?"))
#saves weight for later use sinve variable weight is changed
orgwt = weight
#asks the user which planet they wish to know their weight on
print("""
What celestial body do you want to know your weight on?
1. Venus
2. Moon
3. Mars
4. Jupiter""")
planet = input ("\nPlease enter your choice. ")
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
    
#figures out which style output is required

if e == 0:
    print("\nPlanet\tPlanet Weight")
    print("Earth",orgwt,sep="\t")
    print(planet,weight,sep="\t")
else:
    print("\n",weight,sep="")



input("\nPress Enter to Exit")
