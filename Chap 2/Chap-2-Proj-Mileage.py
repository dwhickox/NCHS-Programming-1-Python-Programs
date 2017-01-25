#David Hickox
#jan 24 17
#Milage Prgm
#Calculates the milage you can get out of a single tank of gas
#variables
#   tank, gas tank size
#   car, the name of the car
#   mpg, miles per gallon the car gets
#   price, cost of gas
#   cost, cost to fill the whole tank
#   distance, total distance the car can travel


#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Milage Program\n")
#has the user input all the variables

car = input("What type of car do you drive? \n")
tank = float(input("What size gas tank does your "+car.title()+" have? \n"))
mpg = float(input("How many miles per gallon does the "+car.title()+" get?\n"))
price = float(input("How much does a gallon of gas cost?\n"))
#does all of the maths
distance = tank * mpg
cost = price * tank
#prints the out come of the maths in the required formats

print("A brand new", car.title(), "can go", distance,"miles on one tank of gas!\n")
print("To fill the tank it will cost you", locale.currency(cost))
#waits for the user to end the program
input("\nPress Enter to Exit")
