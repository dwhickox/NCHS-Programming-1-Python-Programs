#David Hickox
#jan 24 17
#Bowling Prgm
#Calculates the Bowling you can get out of a single tank of gas
#variables
#   kim1-3, holds the scores for kim
#	kourt1-3, holds the scores for kourtney
#	poptart1-3, holds Mr. Hayes' scores
#	epstein1-3, holds Mrs. Epstein's scores
#	kimave, kim's average
#	kourtave, kourtney's average
#	poptartave, Mr. Hayes' average
#	epsteinave, Mrs. Epstein's average
#	kimney, the team scores for kim and kourtney
#	popstein, the team scores for Mr. Hayes and Mrs. Epstein

#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Bowling Program\n")
#initializes all the values
kim1 = 101
kim2 = 126
kim3 = 132
kourt1 = 135
kourt2 = 117
kourt3 = 123
poptart1 = 199
poptart2 = 218
poptart3 = 221
epstein1 = 220
epstein2 = 197
epstein3 = 236

# the maths for the averages
kimave = (kim1+kim2+kim3)/3
kourtave = (kourt1+kourt2+kourt3)/3
poptartave = (poptart1+poptart2+poptart3)/3
epsteinave = (epstein1+epstein2+epstein3)/3
#maths for team scores
kimney = kim1+kim2+kim3+kourt1+kourt2+kourt3
popstein = poptart1+poptart2+poptart3+epstein1+epstein2+epstein3

#prints the results in a well formated mannor

print ("PLAYER\t\t\t\tAVERAGE")
print ("Kim Kardashian\t\t\t%.3f"%kimave)
print ("Kourtney Kardashian\t\t%.3f"%kourtave)
print ("Mr. Hayes\t\t\t%.3f"%poptartave)
print ("Mrs. Epstein\t\t\t%.3f"%epsteinave)
print ("\nTEAM\t\t\t\t SCORE")
print ("Kim and Kourtney Kardashian\t",kimney)
print ("Mr. Hayes and Mrs. Epstein\t",popstein)
#waits for the user to end the program
input("\nPress Enter to Exit")
