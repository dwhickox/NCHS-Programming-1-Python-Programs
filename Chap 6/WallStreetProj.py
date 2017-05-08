"""calculates the value of an investment after a given time frame"""

import locale
locale.setlocale(locale.LC_ALL, '')
#use locale.currency(var, symbol=True, grouping=True) for currency formating


#def func:
def create():
    """creates the list"""
    global stocks
    stocks = [["Columbia Sportswear", 15], ["Dean Foods", 20], ["Harley Davidson", 12]]
def inputfunc():
    """asks the user to input all of their data"""
    for i in enumerate(stocks):
        stocks[i[0]].append(float(input("What is the current value of "+i[1][0]+"? ")))
def calc():
    """calculates total value of the investment"""
    for i in enumerate(stocks):
        stocks[i[0]].append(i[1][1]*i[1][2])
def printfunc():
    """Prints the data"""
    print("\nCompany Name\t# of Shares\tPrice\tCurrent Value\n")
    for i in stocks:
        # this is here because if something is changed in change when this
        # reruns the list will be an item longer
        if len(i) == 4:
            name, shares, price, value = i
        else:
            name, shares, price, oldvalue, value = i
        if len(name) > 15:
            print(name, shares, locale.currency(price, symbol=True, grouping=True),
                  locale.currency(value, symbol=True, grouping=True), sep="\t")
        else:
            print(name+"\t", shares, locale.currency(price, symbol=True, grouping=True),
                  locale.currency(value, symbol=True, grouping=True), sep="\t")
def changes():
    yn = input("Are there any changes to your portfolio? (y/n)")
    temp = 0
    if yn.lower() == "y":
        company = (input("Which company's shares changed? ")).title()
        for i in enumerate(stocks):
            if company in i[1]:
                temp = 1
                stocks[i[0]][1] = int(input("How many shares of "+company+" do you own now? "))
                print ("Your records have been updated")
                calc()
                printfunc()
        if temp == 0:
            print("Sorry you do not own any of that company")

#def main:
def main():
    """runs the whole program"""
    create()
    inputfunc()
    calc()
    printfunc()
    changes()

#David Hickox
#May 7 17
#Money Bags
#calculates things about investments.
#variables
#   
#functions:
#   inputfunc, asks for all the info]
#   calc, finds the total worth of the companies
#   printfunc, prints everything

print("Welcome to the Money Bags Program\n")

main()

input("\nPress Enter to Exit")
