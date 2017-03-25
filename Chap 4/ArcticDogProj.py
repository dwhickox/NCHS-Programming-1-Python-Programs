"""
#David Hickox
#Mar 20 17
#Arctic Dog Program
#This will display how many snowmobiles were sold
#variables
#   array= an array with months in column zero and number sold in column 1
"""

print("Welcome to the Artic Dog program")
#initializes the array hight and with variables
H = 12
W = 2
#initialises the array, dont really need this but I like it
ARRAY = [[0 for Y in range(H)] for X in range(W)]
# assigns all the values
ARRAY[0] = ["January", "Febuary", "March", "April", "May", "June"]
#split to make pylint happy (maintain an acceptable line lenght)
ARRAY[0] += ["July", "August", "September", "October", "November", "December"]
ARRAY[1] = [28, 30, 24, 10, 12, 10, 5, 3, 4, 10, 21, 25]
#prints header
print("\nMonth\t\t\tSales\n")
#handels all of the logic to print the correct strings
for i in enumerate(ARRAY[0]):
    #ajusts lenght of months
    if len(ARRAY[0][i[0]]) < 8:
        ARRAY[0][i[0]] += "\t"
    #adds tab for spacing
    ARRAY[0][i[0]] += "\t"
    #adds correct amount of asterisks
    ARRAY[0][i[0]] += "*"*ARRAY[1][i[0]]
    #prints end result
    print(ARRAY[0][i[0]])

input("\nPress enter to exit!")
