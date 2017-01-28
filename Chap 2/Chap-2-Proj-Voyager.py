#David Hickox
#Jan 28 17
#Voyager Prgm
#Calculates the position of voyager and round trip time of radio comunication given a date after 
#variables
#	initiald, the initial distance at 9/25/2009
#	mph, how fast the space craft is going in mph
#	days, days after 9/25/09
#	calcdm, calculated distance in miles
#	calcdk, calculated dist in kilo
#	calcda, calculated dist in au
#	time, time it takes for radio waves to travel back and forth

#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Voyager 1 Program\n")
#initializes all the values
initiald = 16637000000
mph = 38241
#ask the user to input the number fo days 
days = int(input("How many days after 09/25/09 do you wish to know postion for? "))
#does the maths
calcdm = initiald + days*24*mph
calcdk = calcdm*1.609344
calcda = calcdm/92955887.6
time = 2*calcdm/670616629

print("The Distance in miles is", calcdm,"Miles")
print("The Distance in kilometers is ", calcdk,"KM")
print("The distance in astronomical units is ",calcda,"AU")
print("The round trip radio communications time is ",time,"Hours")

input("\nPress Enter to exit")
