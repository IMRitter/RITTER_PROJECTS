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

print("Ian Ritter's Tip Calculator App") #App Title
print()
cost_of_meal = float(input("Cost of meal: ")) #The cost of the meal
tip_percentage = float(input("Tip Percent: ")) #How much of a tip
print()
tip_amount = cost_of_meal * (tip_percentage  / 100) #Tip Calculation
print("Tip amount: " + str(round(tip_amount, 2))) #Tip Amount
total_amount = cost_of_meal + tip_amount #Total price of meal calculation
print("Total amount: " + str(round(total_amount, 2))) #Total cost of meal
      
