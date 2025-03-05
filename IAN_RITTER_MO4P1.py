#Name: (IAN RITTER)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 08 JUNE 2024
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Ian Ritter's Letter Grade Converter") #Intro to grade converter app
print()
choice = "y"
while choice.lower() == "y": #While loop
    number = int(input("Enter numerical grade: ")) #User inputs grade score

    # Number score correlates to a letter grade
    if 94 <= number <= 100:
        letter = "A"
    elif 90 <= number <= 93:
        letter = "A-"
    elif 87 <= number <= 89:
        letter = "B+"
    elif 83 <= number <= 86:
        letter = "B"
    elif 80 <= number <= 82:
        letter = "B-"
    elif 77 <= number <= 79:
        letter = "C+"
    elif 73 <= number <= 76:
        letter = "C"
    elif 70 <= number <= 72:
        letter = "C-"
    elif 67 <= number <= 69:
        letter = "D+"
    elif 63 <= number <= 66:
        letter = "D"
    elif 60 <= number <= 62:
        letter = "D-"
    else:
        letter = "E"

    print(f"Letter grade: {letter}") #Depicts Grade based on entry
    print()

    choice = input("Continue? (y/n): ") #User chooses to continue or not
    print()

print("Bye!")

    


