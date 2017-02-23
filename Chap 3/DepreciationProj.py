#David Hickox
#Feb 23 17
#DeprecationPrgm
#calculates total money donated, and averages it
#variables
#   cost, the cost of the machine
#   name, name of the machine
#   svalue, salvage value
#   ul, usefull life
#   cont, if the user wants to continue or not
#   dep, depreciation of the machinery


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Depreciation Program\n")

cont = "y"

while cont.lower() == "y" or cont.lower() == "yes" or cont == "1":
    #askes the user to input all of the information nesisary for the program to run
    name = input("What is the name of this machine? ")
    cost = float(input("What did the machinery cost you? "))
    svalue = float(input("What is the scrap value of the machinery? "))
    ul = float(input("What is the useful life of this in years? "))
    #deos the math to find the yearly deprecaition
    dep = (cost-svalue)/ul
    #prints the result
    print("\nGreat Ep-Hick Company")
    print("Accounting Department\n")
    print ("Name:\t\t"+name.title())
    print ("Cost:\t\t"+locale.currency(cost))
    print ("Scrap Value:\t"+locale.currency(svalue))
    print ("Usefull Life:\t"+str(ul),"Years")
    print("Depreciation:\t"+locale.currency(dep))
    #askes the user if they would like to continue
    cont = input("\nWould you like to continue Y/N? ")

input("Press entrer to exit")

