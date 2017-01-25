#David Hickox
#Jan 24 17
#Chap 2 Proj 2
#joins your two favorite foods
#variables
#   food1, the first favorite food
#   food2, the second favorite food
#   creation, the magical end creation

#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Food Creation Program\n")  
#quereys user for the two food names
food1 = input("What is your favorite food? ")
food2 = input("What is your second favorite food? ")
#adds the two foods together as strings
creation = food1+food2
#prints the end result
print("You should really try", creation.title()+", it sounds great!")





input("\nPress Enter to Exit")
