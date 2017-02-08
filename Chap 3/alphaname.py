name1 = input("What is the first name? ")
name2 = input("What is the second name? ")

if name1.lower() < name2.lower():
    print(name1.title())
    print(name2.title())
else:
    print(name2.title())
    print(name1.title())
