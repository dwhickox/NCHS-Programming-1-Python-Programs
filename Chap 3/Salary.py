#David Hickox
#Feb 15 17
#would be great id i had a title
#descriptions, description, much descripticve
#variables
#   name, users name
#   hrs, hrs worked
#   sal, amount of money made
#   ans, whether or not the user wishes to continue (sentry)


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Salary Program\n")
ans = "y"
while ans.lower() == "y" or ans.lower() == "yes" or ans.lower() == "sure"
    name = input("What is your name? ")
    hrs = float(input("How many hours did you work? "))
    sal = 15*hrs
    print (name.title(), "made", locale.currency(sal), "over the time period of", hrs, "hours")
    ans = input ("Would you like to continue (y, n)? ")




input("\nPress Enter to Exit")
