#David Hickox
#Jan 23/17
#college program
#tells the person what college the were going to and tuition 
#variables
#   college = college name
#   tuition = yearly cost
#   room = yearly cost of room and board
#   years = how many years the person is staying
#   yeartotal = total cost for one year
#   total = total cost over the number of years stayed

#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the College Cost Calculator Program\n")

college = input("What college are you going to? ")
tuition = float(input("What is the yearly tuition at " + college.title()+'? '))
room = float(input("What is the yearly room and board cost at " + college.title()+'? '))
years = float(input("How many years are you studing at "+college.title()+" for? "))

yeartotal = tuition+room
total = yeartotal*years

print(college.title(),"will cost you", locale.currency(yeartotal), "per year\nOr a total of", locale.currency(total), "\nYeah, college is expensive")

input("\nPress Enter to Exit")
