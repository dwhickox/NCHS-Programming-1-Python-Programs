#David Hickox
#Pls put date here ktnxby
#Voting
#Figures out how many votes a canidate has
#variables
#   votestemp holds individual days of voting totals
#   votestotal all the votes cast total
#   numdays number of days votes wer cast on 


#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency(var, symbol=True, grouping=True) for currency formating
print("Welcome to the Voting Program\n")
votestemp = 1
votestotal = 0
numdays = 1


print("press enter when you are finished entering in the votes")
#has the user input infor
while votestemp:
    votestemp = input("How many votes were cast on day "+str(numdays)+"? ")
    if votestemp:
        votestotal += float(votestemp)
        numdays += 1
    else:
        print("exiting now")
        numdays -= 1
#does the math and prints the output
print('the total number of votes you have is',votestotal)
print('the average number of votes per day was', votestotal/numdays)




input("\nPress Enter to Exit")
