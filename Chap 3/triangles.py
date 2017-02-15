#David Hickox
#Feb 10 17
#the triangle prgm
#descriptions, description, much descripticve
#variables
#    side1-3, side lenghts
#    msg, the messahe that prints at the end 

print("Welcome to the Triangle Program\n")

#asks user for the lenghts of the triangle sides

side1 = float(input("What is the lenght of the first side of the triangle? "))
side2 = float(input("What is the lenght of the second side of the triangle? "))
side3 = float(input("What is the lenght of the third side of the triangle? "))


# determines the shape of the triangle

if abs(side1)==abs(side2) and abs(side2)==abs(side3):
    msg="Equilateral"
elif abs(side2)==abs(side1) or abs(side2)==abs(side3) or abs(side1)==abs(side3):
    msg="Isosceles"
elif abs(side1)!=abs(side2) and abs(side2)!=abs(side3) and abs(side1)!=abs(side3):
    msg="Scalene"
else:
    msg="You Broke Something!"

#displayes the triangle
print("A triangle with side lenghts:", side1,side2,"and",side3,"will be a", msg,"triangle")




input("\nPress Enter to Exit")
