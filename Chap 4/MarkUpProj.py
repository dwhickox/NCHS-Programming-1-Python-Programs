"""
#David Hickox
#Mar 14 17
#Mark Up Program
#This will calculate the markup for some toys
#variables
#   ARRAY just creates the table, column 1 week, column 2 gallons column 3 - miles, column 4 mpg
"""

import locale
#imports date time and curency handeling (this takes the place of #$%.2f"%)
locale.setlocale(locale.LC_ALL, '')
#use locale.currency(var, symbol=True, grouping=True) for currency formating
H = 6
W = 6
ARRAY = [[0 for x in range(H)] for y in range(W)]
print("Welcome to the MPG Program\n")
ARRAY[1][1] = "Teddy Bear"
ARRAY[1][2] = 12.5
ARRAY[2][1] = "Toy Train"
ARRAY[2][2] = 58.75
ARRAY[3][1] = "Hoola Hoop"
ARRAY[3][2] = 10
ARRAY[4][1] = "Betsy Wetsy"
ARRAY[4][2] = 15
ARRAY[5][1] = "Pogo Stick"
ARRAY[5][2] = 11

print("Item\t\tCost\tMarkup\tRetail")
for i in range(1, 6):
    ARRAY[i][3] = ARRAY[i][2]*1.4
    ARRAY[i][4] = ARRAY[i][2]*.4
    print(ARRAY[i][1], locale.currency(ARRAY[i][2]), sep="\t", end="\t")
    print(locale.currency(ARRAY[i][4]), locale.currency(ARRAY[i][3]), sep="\t", end="\n")

input("press enter to exit!")
