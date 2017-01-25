#David Hickox
#Joint army navy (JAN) 19 2017
#Icecream
#Total cost of ice cream cones
#variables
#   Number = number of cones
#   Cost = cost of one cone
#   tax = tax as a decimal
#   total = total cost of all the cones

number = 3 
cost = .75
tax =.06


#prints welcome
print("Welcome to the Icecream Calculator Program\n")

#does the math

total = (number*cost)*(1+tax)

print("The", number,"cones will cost you $%.2f"% total)




input("\nPress Enter to Exit")
