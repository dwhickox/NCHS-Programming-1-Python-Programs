# This program computes the final value of an invested
# amount using the compound interest formula:
# amount = principle * (1 + rate / num) ** (num * term)

#   Variables:
#      amount ........... Final value of investment
#      principle ........ Amount invested
#      rate ............. Rate of interest as a decimal
#      num .............. Number of times per year compounded
#      term ............. Investment term in years
#      percentagerate ... Rate of interest as a percentage
import locale
locale.setlocale( locale.LC_ALL, '' )
# welcome message
print ("Welcome to the Investing Program \n")

#   Assign values of input data

principle = 4500
percentagerate = .096
term = 2
num = 4
#   Compute final value of investment
rate = percentagerate * 100
amount = principle * (1 + percentagerate / num) ** (num * term)


#   Display results

print ("Amount of money invested ....", principle, "dollars")
print ("Rate of interest ............", rate, "percent")
print ("Frequency of compounding ....", num, "times per year")
print ("Period of investment ........", term, "years")
print ()
print ("Final value of investment ...", locale.currency(amount), "dollars")

input("\nPress enter to exit")
