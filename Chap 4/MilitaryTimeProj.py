"""
#David Hickox
#Mar 24 17
#Military Time Program
#This will display military times, standard times, and time from midnight in minutes
#variables
#   mil_time = a list of times and other garbled nonsence
#   array = an array with military times in column 0, Standard
#       time in column 1, and minutes from midnight in column 2
#   hrslice = the hour information
#   minslice = the min information
"""
#adds values to MIL_TIME
MIL_TIME = ("00:45", "15:10", "20:03", "HH,MM", "17:36", "09:48")
#split to make pylint happy
MIL_TIME += ("10:11", "XX:09", "11:09", "10:04", "04:20", "05:09", "!8:$4")
#initializes the array hight and with variables
H = 13
W = 3
#initialises the array, dont really need this but I like it
ARRAY = [[0 for Y in range(H)] for X in range(W)]
print("Welcome to the Military time program")
print("\nMilitary Time\tStandard Time\tMinutes from Midnight")
#does all of the logic for the program
for i in enumerate(MIL_TIME):
    #checks to see if the time is actualy a time and not garbage
    if MIL_TIME[i[0]][0:2].isdigit() and MIL_TIME[i[0]][3:5].isdigit():
        #stores military time
        ARRAY[0][i[0]] = MIL_TIME[i[0]]
        #stores the hours
        HRSLICE = MIL_TIME[i[0]][0:2]
        #store the min
        MINSLICE = MIL_TIME[i[0]][3:5]
        #store minutes from midnight
        ARRAY[2][i[0]] = str(int(HRSLICE)*60+int(MINSLICE))
        #changes hours to 12 hour time intead of 24
        if int(HRSLICE) > 12:
            HRSLICE = str(int(HRSLICE)-12)
        #changes 00 to 12
        if int(HRSLICE) == 0:
            HRSLICE = "12"
        #gets rid of the extra zero ahead of times of less than 10 hours
        if HRSLICE[0] == "0":
            HRSLICE = HRSLICE[1]
        #store 12 hour time
        ARRAY[1][i[0]] = HRSLICE+":"+MINSLICE
        #prints all the information
        print(ARRAY[0][i[0]], ARRAY[1][i[0]], ARRAY[2][i[0]], sep="\t\t")

input("\nPress Enter To Exit")
