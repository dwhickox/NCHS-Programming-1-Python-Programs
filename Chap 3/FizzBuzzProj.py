#David Hickox
#Feb 28 16
#FizzBuzz
#Prints numbers, but any multiples of 3 print fizz, and any multiples of 5
#print buzz, and multiples of both print fizzbuzz
#variables
#   count, sentry
#this works since n % k returns if there is a remainder from n/k, if there is it
#will not equal zero proving n is not a multiple of k, so I check to see if it
#equals 0, pretty simple actualy
print("Welcome to the FizzBuzz Program\n")
#initializes coutn for the while
count = 1
#runs while
while count < 101:
    #checks for multiples and prints an
    if count%3==0 and count%5==0:
        print("FizzBuzz")
    elif count%3==0:
        print("Fizz")
    elif count%5==0:
        print("Buzz")
    else:
        print(count)
    count+=1
input("\nPress Enter to Exit")
