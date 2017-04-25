"""
#David Hickox
#April 24 17
#DMV
#this will see if the license plate checked is infact a criminal
#variables
#   Criminals, list of said criminals
#   Item, each item in the for loop
#   I, Check variable for the if, too see if a criminal was found or not
"""
I = 0
CRIMINALS = [["David Hickox", "H12345", 11], ["Zack Mikos", "M67890", 8],
             ["Shoshanna Perchanok", "P45678", "2"], ["Jimmie Schatz", "S23456", 10],
             ["Erika Christensen", "C90123", 5], ["Trevor Pavelka", "P78901", 15],
             ["Christina Vasquez", "V34567", 7], ["Zach Kunzer", "K56789", 4]]
print("Welcome to the DMV program")
PLATE = (input("\nWhat is the license plate number? ")).upper()
for ITEM in CRIMINALS:
    if ITEM[1] == PLATE:
        print("\nNaperville trouble maker:", ITEM[0])
        print("Outstanding Warrents:", ITEM[2])
        print("\nPULL THIS PERSON OVER IMMIEDIATLY AND ARREST THEM!")
        I = 1
if I == 0:
    print("\nThese are not the droids you are looking for :(")

input("\nPress Enter to exit")
