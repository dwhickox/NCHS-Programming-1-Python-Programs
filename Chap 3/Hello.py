#David Hickox
#Hello
#would be great id i had a title
#choose a language to display hello in
#variables
#   lang, the selection for language
#   message, the way they say hello, what prints
#   rerun, checks to see if they would like to run the program again

#creates array if needbe
#array = [[0 for x in range(h)] for y in range(w)] 
#imports date time and curency handeling because i hate string formating (this takes the place of #$%.2f"%) 
import locale
locale.setlocale( locale.LC_ALL, '' )
#use locale.currency() for currency formating
print("Welcome to the Hello Program")

print("""
|--------------------|
|For English Press 1 |
|--------------------|
|For Spanish Press 2 |
|--------------------|
|For French Press 3  |
|--------------------|
|For German Press 4  |
|--------------------|
""")
i = 1
while i > 0:
    lang = input("\nWhat language do you wish to see \"hello displayed\" in? ")
    
    if lang.lower() == "english" or lang.lower() == "1":
        message = "\nEnglish -- Hello"
    elif lang.lower() == "spanish" or lang.lower() == "2":
        message = "\nSpanish -- Hola"
    elif lang.lower() == "french" or lang.lower() == "3":
        message = "\nFrench -- Bonjour"
    elif lang.lower() == "german" or lang.lower() == "4":
        message = "\nGerman -- Guten Tag"
    else:
        message = "\nthis was not an option, please try again"

    print(message)

    rerun = input("\nWould you like to re-run the prigram (Y/N)? ")

    if rerun.lower() == "n" or rerun.lower() == "0" or rerun.lower() == "no":
        i = 0


input("\nPress Enter to Exit")
