#David Hickox
#Feb 16 17
#ticket cost
#calculates ticket cost tabel
#variables
#   i = sentry variable
#   cost = total cost for num of tickets

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Ticket Cost Program\n")
i = 1
cost = 0
print("Number of tickets\tTotoal Cost of Tickets")
while i <= 12:
    cost = 10.75* i
    print(i,locale.currency(cost),sep='\t\t\t')
    i += 1



input("\nPress Enter to Exit")
