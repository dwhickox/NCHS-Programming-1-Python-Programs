#David Hickox
#Feb 13 17
#Tax
#Calculates income tax for an income
#variables
#   income, the income of the person in question
#   taxtot, the tax they pay
#   e, my lazy way of handeling the else since you cant currentcy format a string 

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Tax Calculation Program\n")
#asks for income
income = float(input("How much did you make this year? "))
#makes e 0 saying the else has not yet been triggered
e = 0
#does the math for the taxes

if income > 0 and income <= 8925:
    taxtot = (.10*income) 
elif income > 8925 and income <= 36250:
    taxtot = (892.5+(.15*(income-8925))) 
elif income > 36250 and income <= 87850:
    taxtot = (4991.25+(.25*(income-36250))) 
elif income > 87850 and income <= 183250:
    taxtot = (17891.25+(.28*(income-87850))) 
elif income > 183250 and income <= 298350:
    taxtot = (44603.25+(.33*(income-183250))) 
elif income > 298350 and income <=400000:
    taxtot = (115586.25+(.35*(income-298350))) 
elif income > 400000:
    taxtot = (116163.75+(.396*(income-400000))) 
else:
    e = 1
    taxtot = "You do not pay taxes, lucky..."
#Print the output in 3 lines unless you put in a negitive number or 0
if e == 1:
    print(taxtot)
else:
    print("Based upon your annual income of", locale.currency(income, symbol=True, grouping=True),"\nYou owe the IRS a total of", locale.currency(taxtot, symbol=True, grouping=True),"\nPlease make your checks payable to Mrs. Epstien")




input("\nPress Enter to Exit")
