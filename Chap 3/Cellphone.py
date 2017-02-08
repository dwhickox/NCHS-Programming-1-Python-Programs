#David Hickox
#Feb 6 17
#Cellphone (call me maybe?)
#the program wil calculate a total cellphone bill
#variables
#   text, how many texts were sent
#   total, bill total

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Cell Phone Program\n")

text = int(input("How many texts did you send? "))

if text > 300:
	 bill = (text-300)*.03+20
else:
	bill = 20

print("The total cost of your bill will be", locale.currency(bill))

input("\nPress Enter to Exit")
