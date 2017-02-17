#David Hickox
#Feb 16 17
#expensive grades
#Calculates the amount of money you owe your teacher doubling how many pennies you give her every day
#variables
#   i, sentry variable
#   total, total amount for a given day
#   totalprev, holds on to everything for all the days


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the pennies are expensive Program\n")

i = 1
total = .01
totalprev = 0

while i <= 30:
    if i == 15 or i == 30:
        print("At day", i," you will have paid the teacher", locale.currency(totalprev, symbol=True, grouping=True))
    totalprev += total
    total = total*2
    i += 1



input("\nPress Enter to Exit")
