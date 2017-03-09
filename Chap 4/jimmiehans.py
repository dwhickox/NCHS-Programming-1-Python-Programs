#David Hickox
#Mar 9 17
#Jimmmie Hans, freaky fast physics
#this will calculate the total of a 15 sandwitch platter
#variables
#   array column 0 is prices
#   array column 1 is choices


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Jimmie Hans Program\n")
#i = 12
array = [[0 for x in range(1)] for y in range(4)] 
array[[0],[0]] = 21.99 #price for the platter
array[[0],[1]] = .5 #price of extra cheese per sand
array[[1],[2]] = 1 #price of xtra meat per sand
array[[1],[0]] = 0 #cheese 
array[[1],[1]] = 0 #meat
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
      array[[1],[2]] = int(input("Sandwitch #"+str(i)+"?")) #stores sand choice
      array[[1],[3]] = input("Extra Cheese?(Y/N) ")#stores if they want extra cheese on this sand or not
      if array[[1],[2]] != 6:
          array[[1],[3]] = input("Extra Meat?(Y/N) ")#stores if they want extra meat
      else:
          array[[1],[3]] = "n"
      #addes to the total in 
      if array[[1],[2]].upper() == "Y":
          array[[1],[0]] += 1
      if array[[1],[3]].upper() == "Y":
          array[[1],[1]] += 1

#total = tax*(baseprice+cheeseextra*chzprice+meatextra*meatprice)
array[[0],[3]] = 1.0175*(array[[0],[0]]+array[[1],[0]]*array[[0],[1]]+array[[1],[1]]*array[[1],[2]])
      
      
input("\nPress Enter to Exit")
