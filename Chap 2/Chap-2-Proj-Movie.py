#David Hickox
#2/2/27
#Movie project
#calculates ticket sales for 3 movies
#variables
#   tp, ticket price
#   movie1-3, the three movie names
#   lnm1-3, length of the movie names
#   lnmax, max length of any of the movie titles
#   lntabmax, how many tabs long the max is
#   lntab1-3, how many tabs long each string is 
#   tickets1-3, the number of tickets sold for those movies
#   total1-3, the total sales
#   print1-4, what the print statements are supposed to say

#Variables defined-----------
tp = 7
#----------------------------

#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating

#welcomes the user
print("Welcome to the Movie Program\n")

#the rest of the variables are inputed here-------------------------------

movie1 = input("What is the name of the first movie? ")
movie2 = input("What is the name of the second movie? ")
movie3 = input("What is the name of the third movie? ")

tickets1 = int(input("\nHow many tickets were sold for "+movie1.title()+"? "))
tickets2 = int(input("How many tickets were sold for "+movie2.title()+"? "))
tickets3 = int(input("How many tickets were sold for "+movie3.title()+"? "))

#--------------------------------------------------------------------------

#gets the lengths of the movie names

ln1 = len(movie1) 
ln2 = len(movie2)
ln3 = len(movie3)

#-----------------------------------

#finds the longest movie title

if ln1 > ln2 and ln1 > ln3:
    lnmax = ln1
if ln2 > ln1 and ln2 > ln3:
    lnmax = ln2
if ln3 > ln2 and ln3 > ln1:
    lnmax = ln3

#----------------------------------

#figures out how long each print statment is 




#Now all the values (total prices) are calculated--------------------------

total1 = tp*tickets1
total2 = tp*tickets2
total3 = tp*tickets3

#--------------------------------------------------------------------------

#Everything is now returned to the user in a well formated mannor----------

print("\nMovie Title\t\t\t Tickets Sold\t Total Sales")
print(movie1.title(),"\t\t\t",tickets1,"\t\t",locale.currency(total1))
print(movie2.title(),"\t\t\t",tickets2,"\t\t",locale.currency(total2))
print(movie3.title(),"\t\t\t\t",tickets3,"\t\t",locale.currency(total3))

#--------------------------------------------------------------------------

input("\nPress Enter to Exit")
