#Name: Ian Ritter
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 06 JULY 2024
#Project #: MO8 P1 
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import tkinter as tk  # tkinter library for GUI
from tkinter import messagebox  # Import messagebox for displaying validation messages
import math  # Import math library for mathematical functions

def calculate_hypotenuse():  # Define the function to calculate the hypotenuse
    try:
        # Get the values from the entry widgets and convert them to float
        a = float(entry_side_a.get())
        b = float(entry_side_b.get())
        
        # Calculate the hypotenuse using the Pythagorean Theorem
        c = math.sqrt(a**2 + b**2)
        
        # Round the result to 3 decimal places
        c = round(c, 3)
        
        # Display the result in the result_label
        result_label.config(text=f"Hypotenuse: {c}")
    except ValueError:
        # Display an error message if the input values are not valid numbers
        messagebox.showerror("Invalid input", "Please enter valid numbers for sides a and b")

# Create the main window
root = tk.Tk()
root.title("Hypotenuse Calculator")

# Setting Window Size
root.geometry("300x200") # W x H

# Create and place the label and entry for side a
label_side_a = tk.Label(root, text="Enter Side A:")
label_side_a.pack()
entry_side_a = tk.Entry(root)
entry_side_a.pack(padx=15, pady=15)

# Create and place the label and entry for side b
label_side_b = tk.Label(root, text="Enter Side B:")
label_side_b.pack(padx=0, pady=1)
entry_side_b = tk.Entry(root)
entry_side_b.pack(padx=15, pady=15)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_hypotenuse)
calculate_button.pack()

# Create and place the label to display the result
result_label = tk.Label(root, text="Hypotenuse:")
result_label.pack()

# Run the main event loop
root.mainloop()
