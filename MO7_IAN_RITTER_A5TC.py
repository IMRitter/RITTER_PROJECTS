#!/usr/bin/env python3

#Name: IAN RITTER
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 29 JUNE 2024
#Project #: MO7 -- ASSIGNMENT 5
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

TAX = 0.06 # TAX RATE AS A CONSTANT

def sales_tax(total): # FUNCTION TO CALCULATE SALES TAX
    sales_tax_amount = total * TAX #TOTAL TAXES PAID BASED ON TOTAL
    return sales_tax_amount

def main(): # MAIN FUNCTION TO EXECUTE THE SALES TAX CALCULATION
    print("Sales Tax Calculator\n") # TITLE FOR THE PROGRAM
    total = float(input("Enter total: ")) #USER INPUT
    total_after_tax = round(total + sales_tax(total), 2) # TOTAL AMOUNT AFTER SALES TAX
    print("Total after tax: ", total_after_tax) # DIPICTING TOTAL AMOUNT
    
if __name__ == "__main__": #ENTRY POINT OF THE PROGRAM
    main()
