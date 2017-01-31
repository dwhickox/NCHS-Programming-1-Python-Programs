#David Hickox
#jan 26 17
#Payroll Prgm
#Calculates the pay for your workers
#variables
#       list is a list of the employeyes name in the order justin jack rohan mike
#	w = width of the array 
#	h = height of the array 
#	array column 1 is pay rate for each person in the above order, and the second column is the hours worked,
#	the third colum is social security, the fourth is tax, fifth is net pay, sixth is gross pay
#	sleep, determines how long the computer sleeps inbetween printing lines, turn this to 0 for word vomit
#	str is the string that is carried from the print slow function input to the deffinition
#	letter is the letter in the string that is being written by sys.stdout
#	i is just the variable that counts for the for loop 

#imports date time and curency handeling because i hate string formating (this takes the place of #$%sleepf"%) 
import locale
import time #time is used in this program to give it an old timey computer feel printing the lines slowly instead of vomiting 4 pay stubs at you rather agressivly
import sys #sys is used to print the strings a single character at a time
locale.setlocale( locale.LC_ALL, '' ) #sets the locale setting to whatever the computer it is running on is set to

#initializes all the values
w = 6 
h = 4
#creates array
array = [[0 for x in range(h)] for y in range(w)] 
#creates the list of names
list = ["Justin Lefkowitz", "Jack Taylor", "Rohan Bhargava", "Micheal Clinkert"]
#i felt like haveing some fun, so this is just meant to slow the program down to make it look like it is being run up on an old machene working hard, set these to 0 to negate their effects
linesleep = .2
charsleep = .02
def print_slow(str): #changes the print statement to print strings on character at at time and adds a delay inbeteen characters and after each line
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(charsleep)
    time.sleep(linesleep)
#enters pay rates
array[0][0] = 8.35
array[0][1] = 15.5
array[0][2] = 13.25
array[0][3] = 13.5

print_slow("Welcome to the Payroll Program\n")

# has the user input the hours,does the math for each person, but instead of copying and pasting 3 times i decided to just use a for loop
for i in range(0, 4):
	print_slow("\nHow many hours did "+list[i]+" work? ")
	array[1][i] = float(input()) ##hrs worked
	array[5][i] = array[0][i]*array[1][i]#gross pay
	array[2][i] = array[5][i]*.07#ss
	array[3][i] = array[5][i]*.15#tax
	array[4][i] = array[5][i]-array[2][i]-array[3][i]#net
#prints the results in a well formated mannor
for i in range(0, 4):
	print_slow("\n\n________________________________________________________________________________\n")
	print_slow("\nName:\t\t\t "+list[i]+"\n")
	print_slow("Payrate:\t\t "+locale.currency(array[0][i])+"\n")
	print_slow("Hours Worked:\t\t %.0f"%array[1][i]+"\n")
	print_slow("Gross Pay:\t\t "+locale.currency(array[5][i])+"\n")
	print_slow("\nDeductions:\n")
	print_slow("\tSocial Security: "+locale.currency(array[2][i])+"\n")
	print_slow("\tFederal Tax:\t "+locale.currency(array[3][i])+"\n")
	print_slow("\nNet Pay:\t\t "+locale.currency(array[4][i])+"\n")
	print_slow("________________________________________________________________________________\n")
	print_slow("\nGreat Epstein Company\n")
	print_slow("440 W. Aurora Avenue\n")
	print_slow("Naperville, IL 60540\n")
	print_slow("\nPay to the Order of: "+list[i]+" \t\t\t\t\t "+locale.currency(array[4][i])+"\n")
	print_slow(format("___________________________\n", '>81'))
	print_slow(format("Mrs. Epstein, Big Boss\n", '>81'))
	print_slow("\n________________________________________________________________________________\n")
#waits for the user to end the program
input("\n\nPress Enter to Exit")
