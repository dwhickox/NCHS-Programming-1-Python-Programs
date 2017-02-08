#David Hickox
#feb 3 2017
#Itunes
#calculates cost of the songs purchased
#variables
#   songs, the number of songs purchased
#   total price

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the (insert name here bumbblefack) Program\n")

songs = int(input("How many songs do you wish to buy? "))

if songs >= 6:
    total = songs*.99
else:
    total = songs*1.29

print("You will pay a total of",locale.currency(total))


input("\nPress Enter to Exit")
