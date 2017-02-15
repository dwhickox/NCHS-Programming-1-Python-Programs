#David Hickox


# Question 1
car = input("What kind of car do you drive?")

if car.lower() == "toyota" or car.lower() == "honda":
    msg = "you drive a fuel efficient car!"
else:
    msg = "you ruin the enviroment"
print(msg)
    
# Question 2
name = input("What is your name?")
savings = float(input("What is your savings account balance?"))
checking = float(input("What is your checking account balance?"))

if savings >= 1500 or checking >= 3000:
    msg = name.title()+" is on the list"
else:
    msg = "this customer is not on the list"
print (msg)

# Question 3
name = input("What is your name?")
idnum = float(input("What is your id number?"))
gender = input("What is your gender?")

if (gender.lower() == "m" or gender.lower() == "male") and (idnum >= 4389 and idnum <= 5588):
    msg = name.title()+" is an employee on the exterminate list"
else:
    msg = "this employee is not on the list"
print(msg)

# Question 4
name = input("What is your name?")
age = float(input("What is your age?"))
gender = input("What is your gender?")

if (gender.lower() == "f" or gender.lower() == "female") and age > 22:
    msg = name.title()+" is the droid you are looking for"
else:
    msg = "this person does not qualify for the search criteria"
print (msg)

# Question 5 
amount = float(input("How much did you spend? "))

if amount >= 50:
    msg = "You get a 20% discount for a final price of "+str(amount-amount*.2)
elif amount >= 25:
    msg = "You get a 10% discount for a final price of "+str(amount-amount*.1)
elif amount > 0:
    msg = "You get a 5% discount for a final price of "+str(amount-amount*.05)
else:
    msg = "You broke something"

print (msg)

#6

print("""
For Los Angeles Press 1
For Chicago     Press 2
For Louisville  Press 3
For New Orleans Press 4
For St. Louis   Press 5
""")
city = input("What city would you like to visit the 6 Flags in?\nPlease enter a number or type the name as seen above ")

if city.lower() == "1" or city.lower() == "los angeles":
    msg = "The ticket price for Los Angeles is $60"
elif city.lower() == "2" or city.lower() == "chicago":
    msg = "The ticket price for Chicago is $70"
elif city.lower() == "3" or city.lower() == "louisville":
    msg = "The ticket price for Louisville is $45"
elif city.lower() == "4" or city.lower() == "new orleans":
    msg = "The ticket price for New Orleans is $50"
elif city.lower() == "5" or city.lower() == "st. louis":
    msg = "The ticket price for St. Louis is $65"
else:
    msg = "that was not an option please try again"

print(msg)

input("Press enter to exit")
