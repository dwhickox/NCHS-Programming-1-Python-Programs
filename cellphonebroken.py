#David Hickox
#Feb 6 17
#Cellphone (call me maybe?)
#the program wil calculate a total cellphone bill
#variables
#   text, how many texts were sent


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
#I DID NOT MESS WITH THIS SINCE YOU DO NOT KNOW HOW TO USE IT
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Cell Phone Program\n")

text = int(input("How many texts did you send? "))

if text <= 300:
    bill = 20
else:
    bill = ((text-300)*.03)+ 20
print("The total cost of your bill will be $%.2f"% bill)


input("\nPress Enter to Exit")
