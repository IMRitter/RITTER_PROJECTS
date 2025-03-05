#Name: (Ian Ritter)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 01 June 2024
#Project #: MO3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Ian Ritter's Registration App") #Displaying app title
print()
first_name = input("First name: ") #First name input
last_name = input("Last name: ") #Last name input
birth_year = input("Birth year: ") #Birth year input
print()
print("Welcome " + first_name + " " + last_name + "!") #Displaying welcome message 
print()
print("Your registration is complete.") #Completed registration message
temp_password = first_name + "*" + birth_year #Outline of password
print("Your temporary password is: " + temp_password) #Displaying password


