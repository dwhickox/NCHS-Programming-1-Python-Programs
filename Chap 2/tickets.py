#David Hickox
#jan 23 17
# Tickets
#calc total tickets based on num of tickets needed
#variables
#   tp, ticket price
#   nt, number of tickets
#   pr, total price
import locale
locale.setlocale( locale.LC_ALL, '' )
tp = 15
nt = 0
pr = 0

print("Welcome to the (insert name here bumbblefack) Program\n")

#asks the user to input number of tickets
nt = float(input("How many tickets do you need? "))


pr = nt*tp

print("The total cost of your order is", locale.currency(pr))
#$%.2f"%

input("\nPress Enter to Exit")
