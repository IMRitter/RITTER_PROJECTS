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

print("Ian Ritter's Pay Check Calculator App") #Displaying app title
print()
hours_worked = float(input("Hours Worked: ")) #Hours worked input
pay_rate = float(input("Hourly Pay Rate: ")) #Hourly pay rate input
print()
gross_pay = hours_worked * pay_rate  #Calculate gross pay
print("Gross Pay: " + str(gross_pay))  #Display gross pay
tax_rate = 0.18  #Current tax rate
print("Tax Rate: " + str(tax_rate * 100) + "%")  #Display tax rate as percentage
tax_amount = gross_pay * tax_rate  # Calculate tax amount
print("Tax Amount: " + str(round(tax_amount, 2)))  # Display tax amount rounded to 2 decimal places
take_home_pay = gross_pay - tax_amount  # Calculate take-home pay
print("Take Home Pay: " + str(round(take_home_pay, 2))) #Displaying take-home pay 















