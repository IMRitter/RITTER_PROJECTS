#Name: (IAN RITTER)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 08 JUNE 2024
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Ian Ritter's Change App") #Intro to program
print()
choice = "y"
while choice.lower()=="y": # While loop which repeats until becomes false
    cents = int(input("Enter number of cents (0-99): ")) #User inputs # of cents
    print()
    #Calculating Quarters
    quarters = cents // 25 
    cents = cents % 25
    #Calculating Dimes
    dimes = cents // 10
    cents = cents % 10
    #Calculating Nickels
    nickels = cents // 5
    cents = cents % 5
    #Calculating Pennies
    pennies = cents

    print(f"Quarters: {quarters}") #Depicting Quarters with result
    print(f"Dimes: {dimes}") #Depicting Dimes with result
    print(f"Nickels: {nickels}") #Depicting Nickels with result 
    print(f"Pennies: {pennies}") #Depicting Pennies with result
    print()
    choice = input("Continue? (y/n): ") #Continue or not
    print()
print("Bye!")   

    


