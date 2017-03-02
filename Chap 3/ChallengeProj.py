#David Hickox
#Feb 28 16
#Challenge
#Finds a spesific palindrome as per the requirments in car talk 
#variables
#   count, sentry

print("Welcome to the Challenge Program\n")

#Starts at 100k because I need 6 digets and the number cannot exist under 99997, since the num +3 has to have 6 digets
#but I know that the number is not 99997-100000 so I just started the count at 100k to save time from starting at 0
count = 100000
end = 0
while count <=999999 and end == 0:
    #checks for the palindromes, yes this could be more efficient, but copy and paste made this fast...
    #first set of parentheses check the first 4 num, second set checks five and, third checks middle four etc. The checks are 2 arguments long except for the last which is 3)
    if (str(count)[2] == str(count)[5] and str(count)[3] == str(count)[4]) and (str(count+1)[1] == str(count+1)[5] and str(count+1)[2] == str(count+1)[4]) and (str(count+2)[1] == str(count+2)[4] and str(count+2)[2] == str(count+2)[3]) and (str(count+3)[0] == str(count+3)[5] and str(count+3)[1] == str(count+3)[4] and str(count+3)[2] == str(count+3)[3]):
        #prints the results, and each on of the palindromes
        print("The droid you are looking for is",count)
        print("First four digets palindrome:\t",count)
        print("First five digets palindrome:\t",count+1)
        print("Middle four didgets palindrome:\t",count+2)
        print("All six digets palindrome:\t",count+3)
        #ends the while to make the program more efficent
        end = 1
    #updates the sentry
    count += 1


input("\nPress Enter to Exit")
