"""calculates the value of an investment after a given time frame"""

import locale
locale.setlocale(locale.LC_ALL, '')
#use locale.currency(var, symbol=True, grouping=True) for currency formating


#def func:
def inputfunc():
    """asks the user to input all of their data"""
    name = input("What is your name? ")
    amount = float(input("How much are you investing? "))
    interest = float(input("What is the annual rate of interest in percent? "))
    times = int(input("How many times a year with this be compounded? "))
    years = int(input("How many years will the term of this investmnet be? "))
    return name, amount, interest, times, years
def calc(temp):
    """calculates total value of the investment after the given time frame"""
    name, amount, interest, times, years = temp
    interest = interest/100
    total = amount*(1+interest/times)**(times*years)
    return name, amount, interest*100, times, years, total
def printfunc(temp):
    """Prints the data"""
    name, amount, interest, times, years, total = temp
    print("\n\nName\t\t\t", name.title())
    print("Principle\t\t", locale.currency(amount, grouping = True))
    print("Rate\t\t\t", str(interest)+"%")
    print("# times Compounded\t", times)
    print("Length of Investment\t",years,"Years")
    print("Final Worth\t\t", locale.currency(total, grouping = True))

#def main:
def main():
    """runs the whole program"""
    yn = 'y'
    while yn.lower() == "y":
        printfunc(calc(inputfunc()))
        yn = input("\nDo you wish to run this again? (y/n) ")
    



#David Hickox
#May 7 17
#Money Bags
#calculates things about investments.
#variables
#   name, the users name
#   amount, the principle
#   interest, the interest rate
#   times, number of times in one year the investment is compounded
#   years, lenth of the investment
#   temp, this allows the functions to be stacked
#functions:
#   inputfunc, asks for all the info]
#   calc, finds the total worth
#   printfunc, prints everything

print("Welcome to the Money Bags Program\n")

main()

input("\nPress Enter to Exit")
