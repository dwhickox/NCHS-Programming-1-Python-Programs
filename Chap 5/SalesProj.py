#David Hickox
#May 2 17
#Chap 5 test
#sorts a list of sales, prints averages and totals
#variables
#   array, Stores the data
#   tot, total sales
#   ave, average

import locale
locale.setlocale( locale.LC_ALL, '' )

print("Welcome to the Chap 5 test Program\n")
tot = 0
array = [["Opalka",11915.98],["Pathak",13344.43],["Mathur",10773.62],["Harmon",23166.84]]
array.sort()
print("\nName\tSales")
for i in enumerate(array):
    print(i[1][0],locale.currency(i[1][1], symbol=True, grouping=True),sep = '\t')
    tot += i[1][1]
ave = tot/len(array)

print("\nTotal\t"+locale.currency(tot, symbol=True, grouping=True))
print("Average\t"+locale.currency(ave, symbol=True, grouping=True))



input("\nPress Enter to Exit")
