#Name: (IAN RITTER)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 08 JUNE 2024
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Ian Ritter's Tip Calculator") #Intro to program
print()
meal_cost = float(input("Cost of meal: ")) #Input meal cost
print()
tip_percentages = [15,20,25] #The tip percentages
for percentage in tip_percentages: #For loop which depicits each tip %
    print(f"{percentage}%")

    tip_percent = percentage / 100 #Tip Percentage Calculation
    tip_amount = round(meal_cost * tip_percent, 2)#Tip calculation
    total = round(meal_cost + tip_amount, 2) #Total Calculation

    print(f"Tip amount: {tip_amount}")#The cost of the tip
    print(f"total amount: {total}")#Amount with tip
    print()
    
