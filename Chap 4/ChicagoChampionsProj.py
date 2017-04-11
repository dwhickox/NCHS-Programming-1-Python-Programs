"""
#David Hickox
#April 11 17
#Chap4 test
# displayes the price of certain tickets and the total to attend all the games
#variables
#   H = hight of ARRAY
#   W = Width of ARRAY
#   ARRAY = holds the names in column 0, holds the prices in column 1, holds the "nicknames" in column 3
#   NUM = number chosen by the user
"""
NUM = -1
H=5
W=3
ARRAY = [[0 for X in range(H)] for Y in range(W)] 
#imports date time and curency handeling 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Chap 4 Test Program\n")
ARRAY[0] = ["Cubs 2016 World Series","Blackhawks 2015 Stanley Cup","White Soc 2005 World Series","Bulls 1998 NBA Championship","Bears 1985 Super Bowl"]
ARRAY[1] = [4700,2200,1200,45,60]
ARRAY[2] = ["Cubs","Blackhawks","White Sox","Bulls","Bears"]

print("Chicago Championships\t\tAverage Ticket Price")
for i in range(len(ARRAY[0])):
    if len(ARRAY[0][i]) > 25:
        print(ARRAY[0][i], locale.currency(ARRAY[1][i], symbol=True, grouping=True), sep='\t')
    else:
        print(ARRAY[0][i], locale.currency(ARRAY[1][i], symbol=True, grouping=True), sep='\t\t')

print("\nTotal cost to attend all games\t"+locale.currency(sum(ARRAY[1]), symbol=True, grouping=True))

while NUM > 4 or NUM < 0:
    NUM = int(input("\nPlease choose a number between 0 and 4! "))

print("\nCongrats you won tickets to the",ARRAY[2][NUM],"game!")

input("\nPress Enter to Exit")
