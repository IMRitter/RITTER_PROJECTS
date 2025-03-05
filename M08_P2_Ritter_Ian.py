#Name: Ian Ritter
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 06 JULY 2024
#Project #: MO8 P2 
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import tkinter as tk  # Import the tkinter library for GUI
from tkinter import messagebox  # Import messagebox for displaying validation messages
import math

def calculate_average():  # Define the function to calculate the average of the scores
    try:
        # Get the values from the entry widgets and convert them to float
        score1 = float(entry_test1.get())
        score2 = float(entry_test2.get())
        
        # Calculate the average of the two scores
        average = (score1 + score2) / 2
        
        # Display the result in the result_label
        result_label.config(text=f"Average: {average:.2f}")
    except ValueError:
        # Display an error message if the input values are not valid numbers
        messagebox.showerror("Invalid input", "Please enter valid numbers for both test scores")

def calculate_total():  # Define the function to calculate the total of the scores
    try:
        # Get the values from the entry widgets and convert them to float
        score1 = float(entry_test1.get())
        score2 = float(entry_test2.get())
        
        # Calculate the total of the two scores
        total = score1 + score2
        
        # Display the result in the result_label
        result_label.config(text=f"Total: {total:.2f}")
    except ValueError:
        # Display an error message if the input values are not valid numbers
        messagebox.showerror("Invalid input", "Please enter valid numbers for both test scores")

# Create the main window
root = tk.Tk()
root.title("Test Score Calculator")

# Set the size of the window
root.geometry("300x250")  # Width x Height

# Create and place the label and entry for test 1
label_test1 = tk.Label(root, text="Test 1 Score:")
label_test1.pack(padx=5, pady=10)
entry_test1 = tk.Entry(root)
entry_test1.pack(padx=6, pady=5)

# Create and place the label and entry for test 2
label_test2 = tk.Label(root, text="Test 2 Score:")
label_test2.pack()
entry_test2 = tk.Entry(root)
entry_test2.pack()

# Create and place the Average button
average_button = tk.Button(root, text="Calculate Average", command=calculate_average)
average_button.pack(padx=10, pady=8)

# Create and place the Total button
total_button = tk.Button(root, text="Calculate Total", command=calculate_total)
total_button.pack()

# Create and place the label to display the result
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=8, padx=7)

# Run the main event loop
root.mainloop()
