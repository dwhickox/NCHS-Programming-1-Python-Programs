#David Hickox
#Mar 14 17
#MPG Program
#this will calculate the mpg of your weekly trips
#variables
#   array just creates the table, column 1 week, column 2 gallons column 3 - miles, calumn 4 mpg

h = 5
w = 5
array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the MPG Program\n")
#sets up week numbers in the array, this is unnessicary in this situation, but decent practice. 
for i in range(5):
    array[1][i] = i
#does the math for each input, using arrays to easily be able to store the data.
for i in range(1,5):
    print("Week",i)
    array[2][i]= float(input("how many gallons of gas did you use this week? "))
    array[3][i]= float(input('How far did you travel this week? '))
    array[4][i]= array[3][i]/array[2][i]
    print ("your mpg is", round(array[4][i],2),"for week",i)
    print()
input("press enter to exit!")
