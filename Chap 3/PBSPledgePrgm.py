#David Hickox
#Feb 22 17
#PBS Pledge
#calculates total money donated, and averages it
#variables
#	donname donators name
#	pledge, one individual pledge amount
#	pledgetot, total of all the pledges
#	numpledge, number of pledges

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating


print("Welcome to the PBS Pledge Program")
#assignes all the values to start the while
donname = "abc"
pledge = 1
pledgetot = 0
numpledge = 0
#runs the while to add up all the pledges
while donname and pledge:
	numpledge += 1
	donname = input("What is the donator's name? (Press enter when finished) ")
	pledge = input("How much did "+donname.title()+" give? (Press enter when finished) ")
	if pledge:
		pledgetot += float(pledge)

#subtracts one from the pledge number because one extra is added when the while loop runs for the last time
numpledge -=1
#prints the end result and does the math for it as well
print("\nThe total dontation is", locale.currency(pledgetot))
print("The average donation is",locale.currency(pledgetot/numpledge),"over a total of", numpledge,"donors")
input("\nPress Enter to Exit")
