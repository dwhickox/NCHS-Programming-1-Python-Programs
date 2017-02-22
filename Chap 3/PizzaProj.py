#David Hickox
#Feb 21 17
#Pizza program
#calculates costs of pizzas
#variables
#	size, size of the pizzas
#	toppings, number of toppings
#	chz, extra cheese, y/n
#	cost, cost of the pizza
# e, the lazy else triggeres are all e with a number after

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Pizza Program")
print("""
6 inch = 1
10 inch = 2
14 inch = 3
16 inch = 4
""")
#my lazy else triggers
e = 0
e1 = 0
#asks user to input what they want
size = input("What size would you like? ")
toppings = int(input("How many toppings do you want? "))
chz = input("Would you like extra cheese, Y/N? ")
#figures out what size pizza the customer wishaes to order
if size == "6" or size == "6 inch" or size == "1":
	#this and all of its copy pasted copyies figure out if the customer wants extra cheese and charges them acordingly
	if chz.lower() == "n" or chz.lower() == "no":
		cost = (4+toppings*.5)*1.06
	elif chz.lower() == "y" or chz.lower() == "yes":
		cost = (5+toppings*.5)*1.06
	else:
		#triggers the wrong cheese selection message
		e1 == 1
elif size == "10" or size == "10 inch" or size == "2":
	if chz.lower() == "n" or chz.lower() == "no":
		cost = (7.5+toppings*.6)*1.06
	elif chz.lower() == "y" or chz.lower() == "yes":
		cost = (8.5+toppings*.6)*1.06
	else:
		e1 == 1
elif size == "14" or size == "14 inch" or size == "3":
	if chz.lower() == "n" or chz.lower() == "no":
		cost = (12.9+toppings*.75)*1.06
	elif chz.lower() == "y" or chz.lower() == "yes":
		cost = (14.9+toppings*.75)*1.06
	else:
		e1 == 1
elif size == "16" or size == "16 inch" or size == "4":
	if chz.lower() == "n" or chz.lower() == "no":
		cost = (14.25+toppings*.9)*1.06
	elif chz.lower() == "y" or chz.lower() == "yes":
		cost = (16.25+toppings*.9)*1.06
	else:
		e1 == 1
else:
	#triggers the wrong pizza size message
	e = 1

#	prints the correctly fromated message based upon the input criteria
if e == 1:
	print("That size pizza is not an available option... please try again")
elif e1 == 1:
	print("Please choose either Y for yes or N for No for cheese, please try again")
elif e == 0 and e1 == 0:
	print("The total for your pizza is ", locale.currency(cost),"\nThank You!")
else:
	#debug
	print("Yours truely broke something, programmers arent perfect what can i say...")

input("\nPress Enter to Exit")
