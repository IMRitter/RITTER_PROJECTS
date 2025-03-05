# pi * user's input (diameter) = circumference
import tkinter as tk
from tkinter import ttk
import math as m 

# Circumference Calculation and set value to entry
def calculateCircumference():
    # calculate the circumference
    circumference = float(diameterValue.get()) * m.pi
    # set the circumference to the entry
    circumferenceValue.set(round(circumference, 3))

# main window
root = tk.Tk()
root.title('Circumference Calculator')

# frame to hold the objects/components
#frame = tk.Frame(root, padding = '10 10 10 10')
#frame.grid(row = 0, column = 0)

# label to prompt the user to enter a diameter value
diameterLabel = ttk.Label(root, text = 'Enter a diameter value: ')
diameterLabel.grid(row = 0, column = 0)

# new variable for diameter value
diameterValue = tk.StringVar()

# entry to retrieve the user's input
diameterEntry = ttk.Entry(root, width=25, textvariable=diameterValue)
diameterEntry.grid(row = 0, column = 1)

#label for the circumference display
circumferenceLabel = ttk.Label(root, text = 'The circumference is: ')
circumferenceLabel.grid(row = 1, column = 0)

# variable to hold the circumference Value
circumferenceValue = tk.StringVar()

# read-only entry to show the circumference
circumferenceEntry = ttk.Entry(root, width=25, state="readonly", textvariable=circumferenceValue)
circumferenceEntry.grid(row = 1, column = 1)

# button for calculate
CalculateButton = ttk.Button(root, text = 'Calculate', 
                            command = calculateCircumference)
CalculateButton.grid(row = 2, column = 0)

# button for exit
exitButton = ttk.Button(root, text = 'Exit', command = root.destroy)
exitButton.grid(row = 2, column = 1 )

# format the components
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10
                         )
root.mainloop()
