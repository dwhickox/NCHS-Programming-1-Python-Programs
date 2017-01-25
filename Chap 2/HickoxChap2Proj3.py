#David Hickox
#Jan 24 17
#Chap2 Proj 3
#Telll the user how much to tip
#variables
#   total, is the resturant total bill
#   tip15, tip at 15 percent
#   tip20, tip at 20 percent

#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Tip Calc Program\n")
#inputs resturant total

total = float(input("What was the total bill? "))

#does the math for the tips
tip15 = total*.15
tip20 = total*.2

print("\nIf you would like to tip 15 percent you should tip", locale.currency(tip15))

print("If you would like to tip 20 percent you should tip", locale.currency(tip20))

input("\nPress Enter to Exit")
