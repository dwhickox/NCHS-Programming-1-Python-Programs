#David Hickox
#Mar 8 17
#Temp Program
#does c to f
#variables
#   c = celsius
#   f = fahrenheit

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Temprature Program\n")
f = 0
print ("Celsius\t  Fahrenheit") 
for c in range(30,41,1):
    f=9*c/5+32
    print(c,"C    =",f,"F")




input("\nPress Enter to Exit")
