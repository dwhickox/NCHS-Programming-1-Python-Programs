"""
#David Hickox
#Mar 24 17
#Send more money
#This will find all the answers to the send more money problem
#variables
#   word = the string
#   wordxx = slices of word
#   wordlist = word just in list form not a sting, makes it adressable
#   numbers = the numbers to replace the letters with
#   i = count variable
#   x = diffrent count
#   next = tells the output if there has already been an answer
#   prev = list of previous answers to prevent duplicats
#   letter = the letter that the program is currently on
#   run = tells the if the while has run
"""
#imports the ability to list out all of the posible combinations of a list
import itertools
#assigns starting values
X = 0
I = 0
RUN = 0
NEXT = 0
PREV = [0]
WORD04 = 1
WORD59 = 2
WORD10 = 0
NUMBERS = list(itertools.permutations(range(10)))
#runs all logic, caped at 10! because that is how many posible combinations of 0-9 there are
while X < 3628800:
    #resets I, word, and wordlist for each try
    WORD = "send more money"
    WORDLIST = list("send more money")
    I = 0
    for LETTER in WORD:
        # replaces all the similar letters with one number, makes sure that the letter is
        # not a space and has not already been replaced
        while WORD.find(LETTER) > -1 and LETTER.lower() != " " and LETTER.isalpha():
            #creates an editable list
            WORDLIST = list(WORD)
            #edits the list
            WORDLIST[WORD.index(LETTER)] = str(NUMBERS[X][I])
            #recompiles list into string
            WORD = "".join(WORDLIST)
            #tells the if that the while has run 
            RUN = 1
        # updates the count if the letter has not already been replaced
        if RUN == 1:
            I += 1
            RUN = 0
    #slices the string into parts and turns them into integers
    WORD04 = int(WORD[0:4])
    WORD59 = int(WORD[5:9])
    WORD10 = int(WORD[10:])
    #incriments counter
    X += 1
    #checks to see if the resukt is valid and not a repeat
    if WORD04 + WORD59 == WORD10 and WORD04 not in PREV:
        #checks to see if there has already been a result if so it prints
        #"or" if not it sets it so that the next time it will
        if NEXT == 1:
            print("\nor\n")
        else:
            NEXT = 1
        #prints the result
        print("", WORD[0:4])
        print("+" + WORD[5:9])
        print("--------")
        print("",WORD[10:])
        #adds the result to prevent duplicates due to the extra numbers in the digit list
        PREV.append(WORD04)
input("Press Enter to Exit!")
