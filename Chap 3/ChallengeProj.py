#David Hickox
#Feb 28 16
#Challenge
#descirptions are much descriptive
#variables
#   count, sentry

print("Welcome to the Challenge Program\n")

count = 100000
end = 0
while count <=999999 and end == 0:
    #checks for the palindromes, yes this could be more efficient, but copy and paste made this fast...
    #first set of parentheses check the first 4 num, second set checks five and, third checks middle four etc. The checks are 2 arguments long except for the last which is 3)
    if (str(count)[2] == str(count)[5] and str(count)[3] == str(count)[4]) and (str(count+1)[1] == str(count+1)[5] and str(count+1)[2] == str(count+1)[4]) and (str(count+2)[1] == str(count+2)[4] and str(count+2)[2] == str(count+2)[3]) and (str(count+3)[0] == str(count+3)[5] and str(count+3)[1] == str(count+3)[4] and str(count+3)[2] == str(count+3)[3]):
        print("The droid you are looking for is",count)
        end = 1
    count += 1


input("\nPress Enter to Exit")
