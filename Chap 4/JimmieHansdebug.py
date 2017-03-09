#David Hickox
#Mar 9 17
#Jimmmie Hans, freaky fast physics
#this will calculate the total of a 15 sandwitch platter
#variables
#   meat = number of xtra meat
#   xchz = i


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Jimmie Hans Program\n")
i = 12
base = 21.99 #price for the platter
chzprice = .5 #price of extra cheese per sand
meatprice = 1 #price of xtra meat per sand
chz = 0 #cheese 
meat = 0 #meat
#menu
print("""
Pepe...............1
Big John...........2
Totally Tuna.......3
Turkey Tom.........4
Vito...............5
Vegi...............6
Remeber to select 5 sandwitches""")

#repeat the order proccess 5 times
for i in range(1,6):
      sand = int(input("Sandwitch #"+str(i)+"?")) #stores sand choice
      xchz = input("Extra Cheese?(Y/N) ")#stores if they want extra cheese on this sand or not
      if sand != 6:
          xmeat = input("Extra Meat?(Y/N) ")#stores if they want extra meat
      else:
          xmeat = "n"
      #addes to the total in 
      if xchz.upper() == "Y":
          chz += 1
      if xmeat.upper() == "Y":
          meat += 1

#total = tax*(baseprice+cheeseextra*chzprice+meatextra*meatprice)
total = 1.0175*(base+chz*chzprice+meat*meatprice)
      
      
input("\nPress Enter to Exit")
