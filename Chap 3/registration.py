#David Hickox
#feb 8 17
#registration prgm
#
#variables
#   grade, what grade they are
#   regdate - the registration date for the user

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the registration Program")
i = 1
while i>0:
    print("""
    For Fresman please press 9
    For Sophomore please press 10
    For Junior please press 11
    For Senior please press 12
    Para espanol entrar 13
    """)
    grade = input("What year are you in school? ")
    
    #assign an appropriate registration date depening on year
    if grade.lower() == "freshman" or grade.lower() == "9":
        regdate = "August 11"
        i=0
    elif grade.lower() == "sophomore" or grade.lower() == "10":
        regdate = "August 12"
        i=0
    elif grade.lower() == "junior" or grade.lower() == "11":
        regdate = "August 13"
        i=0
    elif grade.lower() == "senior" or grade.lower() == "12":
        regdate = "August 14"
        i=0
    else:
        regdate = "Error, please rerun the program"
    
    # displays the correct registration date
    print ("\nYour registration date is")
    print (regdate)



input("\nPress Enter to Exit")
