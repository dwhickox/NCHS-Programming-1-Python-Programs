"""
#David Hickox
#April 21 17
#Employee Salary
#this will calculate the total salaries, average saleries and employees above and below average
#variables
#   EMPLOYEES = the array that storse all of the employee data
#   temp= temp employee data
#   cont = whether or not to continue the while loop
#   tempn = temp name
#   temps = temp Salary
#   Num = num of employees
#   above = people above average
#   below = below average
#   equal = same as average
"""
import locale
locale.setlocale(locale.LC_ALL, '')
#use locale.currency(var, symbol=True, grouping=True) for currency formating

print("Welcome to the Employee Salary program")
EMPLOYEES = []
TEMPN = 0
TEMPS = 0
CONT = "y"
NUM = 0
ABOVE = [0]
BELOW = [0]
EQUAL = [0]
#lets the user input the emplayees
while CONT.upper() == 'Y':
    TEMPN = (input("What is the employee's name? ")).title()
    TEMPS = float(input("what is the employee's salary? "))
    TEMP = [TEMPN, TEMPS]
    EMPLOYEES.append(TEMP)
    NUM += 1
    CONT = input("Would you like to continye y/n? ")
#print for debug
#print(EMPLOYEES)
#does the math for total and ave Salary
TOT = sum(ROW[1] for ROW in EMPLOYEES)
AVE = TOT/NUM
print("\nTotal salary:", locale.currency(TOT, symbol=True, grouping=True))
print("Average salary;", locale.currency(AVE, symbol=True, grouping=True))
#figures out which emplayees fit in each catagory
for I in EMPLOYEES:
    if I[1] > AVE:
        ABOVE[0] += 1
        ABOVE.append([I[0]])
    if I[1] == AVE:
        EQUAL[0] += 1
        EQUAL.append([I[0]])
    if I[1] < AVE:
        BELOW[0] += 1
        BELOW.append([I[0]])
#prints the employees that fit in each catagory and prints that there are
#no employees that fit if there are none
print("\nNumber of employees making more than average:", ABOVE[0])
if ABOVE[0] == 0:
    print("No employees make above average")
I = 0
for ITEM in ABOVE:
    if I == 0:
        I += 1
    else:
        print(ITEM[0])
print("\nNumber of employees making average:", EQUAL[0])
if EQUAL[0] == 0:
    print("No employees make average")
I = 0
for ITEM in EQUAL:
    if I == 0:
        I += 1
    else:
        print(ITEM[0])
print("\nNumber of employees making less than average:", BELOW[0])
if BELOW[0] == 0:
    print("No employees make below average")
I = 0
for ITEM in BELOW:
    if I == 0:
        I += 1
    else:
        print(ITEM[0])
input("\n\nPress Enter to exit")
