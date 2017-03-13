username = input("what do you want as a username?")
pas=""
while len(pas) < 8:
    pas=input("Please choose a password that is at least 8 charachters long")

amount = int(input("how many students do you have in the class?"))

tot = 0
for i in range(1,amount+1, 1):
    test = float(input("score for student number"+str(i)+":"))
    tot += test

ave = tot/amount
print (ave)
