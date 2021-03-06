#David Hickox
#jan 24 17
#Payroll Prgm
#Calculates the pay for your workers
#variables
#   list is a list of the employeyes name in the order justin jack rohan mike
#	w = width of the array 
#	h = height of the array 
#	array column 1 is pay rate for each person in the above order, and the second column is the hours worked,
#	the third colum is social security, the fourth is tax, fifth is net pay, sixth is gross pay
#	i is just the variable that counts for the for loop 

#imports date time and curency handeling because i hate string formating (this takes the place of #$%sleepf"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Payroll Program")
#initializes all the values
w = 6 
h = 4
#creates array
array = [[0 for x in range(h)] for y in range(w)] 
#creates the list of names
list = ["Justin Lefkowitz", "Jack Taylor", "Rohan Bhargava", "Micheal Clinkert"]
#enters pay rates
array[0][0] = 8.35
array[0][1] = 15.5
array[0][2] = 13.25
array[0][3] = 13.5

# has the user input the hours,does the math for each person, but instead of copying and pasting 3 times i decided to just use a for loop
for i in range(0, 4):
	array[1][i] = float(input("\nHow many hours did "+list[i]+" work? ")) ##hrs worked
	array[5][i] = array[0][i]*array[1][i]#gross pay
	array[2][i] = array[5][i]*.07#ss
	array[3][i] = array[5][i]*.15#tax
	array[4][i] = array[5][i]-array[2][i]-array[3][i]#net
#prints the results in a well formated mannor
for i in range(0, 4):
	print("\n\n________________________________________________________________________________")
	print("\nName:\t\t\t",list[i])
	print("Payrate:\t\t",locale.currency(array[0][i]))
	print("Hours Worked:\t\t %.0f"%array[1][i])
	print("Gross Pay:\t\t",locale.currency(array[5][i]))
	print("\nDeductions:")
	print("\tSocial Security:",locale.currency(array[2][i]))
	print("\tFederal Tax:\t",locale.currency(array[3][i]))
	print("\nNet Pay:\t\t",locale.currency(array[4][i]))
	print("________________________________________________________________________________")
	print("\nGreat Epstein Company")
	print("440 W. Aurora Avenue")
	print("Naperville, IL 60540")
	print("\nPay to the Order of:",list[i],"\t\t\t\t\t",locale.currency(array[4][i]))
	#the format statements right align the text
	print(format("___________________________", '>80'))
	print(format("Mrs. Epstein, Big Boss", '>80'))
	print("\n________________________________________________________________________________")
#waits for the user to end the program
input("\n\nPress Enter to Exit")
