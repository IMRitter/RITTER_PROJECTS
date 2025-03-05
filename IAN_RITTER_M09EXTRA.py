#Name: (Ian Ritter)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 13 JULY 2024
#Project #: M09 Extra Credit
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import tkinter as tk  # Import tkinter for GUI elements
from tkinter import messagebox  # Import messagebox for dialogs
from tkinter import simpledialog  # Import simpledialog for input dialogs

# Define the InventoryApp class
class InventoryApp:
    def __init__(self, root):  # Initialize the main application window
        self.root = root  # Set the root window
        self.root.title("Inventory Management System")  # Set the window title
        
        self.inventory = ["staff", "wand", "potion"]  # Initialize inventory with default items
        
        self.create_widgets()  # Call function to create GUI widgets
    
    def create_widgets(self):  # Define function to create GUI widgets
        title_label = tk.Label(self.root, text="Welcome to the Inventory Management System", font=("Helvetica", 16))  # Create title label
        title_label.pack(pady=10)  # Pack the title label with padding
        
        button_frame = tk.Frame(self.root)  # Create a frame for buttons
        button_frame.pack(pady=10)  # Pack the frame with padding
        
        show_button = tk.Button(button_frame, text="Show", command=self.show_inventory)  # Create Show button
        show_button.grid(row=0, column=0, padx=5)  # Place Show button in grid
        
        grab_button = tk.Button(button_frame, text="Grab", command=self.grab_item)  # Create Grab button
        grab_button.grid(row=0, column=1, padx=5)  # Place Grab button in grid
        
        edit_button = tk.Button(button_frame, text="Edit", command=self.edit_item)  # Create Edit button
        edit_button.grid(row=0, column=2, padx=5)  # Place Edit button in grid
        
        drop_button = tk.Button(button_frame, text="Drop", command=self.drop_item)  # Create Drop button
        drop_button.grid(row=0, column=3, padx=5)  # Place Drop button in grid
        
        exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit)  # Create Exit button
        exit_button.grid(row=0, column=4, padx=5)  # Place Exit button in grid
        
        self.inventory_text = tk.Text(self.root, height=10, width=50, state='disabled')  # Create text area for inventory display
        self.inventory_text.pack(pady=10)  # Pack the text area with padding
        
    def show_inventory(self):  # Define function to show inventory
        self.inventory_text.config(state='normal')  # Enable text area for editing
        self.inventory_text.delete('1.0', tk.END)  # Clear the text area
        self.inventory_text.insert(tk.END, "Inventory:\n")  # Insert inventory title
        for number, item in enumerate(self.inventory, start=1):  # Loop through inventory items
            self.inventory_text.insert(tk.END, f"{number}. {item}\n")  # Insert item number and name
        self.inventory_text.config(state='disabled')  # Disable text area to make it read-only
    
    def grab_item(self):  # Define function to grab an item
        if len(self.inventory) >= 4:  # Check if inventory has 4 or more items
            messagebox.showwarning("Warning", "You can't carry any more items. Drop something first.")  # Show warning message
        else:  # If inventory has less than 4 items
            item = simpledialog.askstring("Grab Item", "Enter the name of the item to grab:")  # Prompt user to enter item name
            if item:  # If user entered an item
                self.inventory.append(item)  # Add item to inventory
                messagebox.showinfo("Item Added", f"{item} was added.")  # Show confirmation message
                self.show_inventory()  # Refresh inventory display
    
    def edit_item(self):  # Define function to edit an item
        number = simpledialog.askinteger("Edit Item", "Enter the number of the item to edit:")  # Prompt user to enter item number
        if number is None or number < 1 or number > len(self.inventory):  # Check if number is invalid
            messagebox.showerror("Error", "Invalid item number.")  # Show error message
        else:  # If number is valid
            item = simpledialog.askstring("Edit Item", "Enter the new name of the item:")  # Prompt user to enter new item name
            if item:  # If user entered a new item name
                self.inventory[number - 1] = item  # Update item in inventory
                messagebox.showinfo("Item Updated", f"Item number {number} was updated.")  # Show confirmation message
                self.show_inventory()  # Refresh inventory display
    
    def drop_item(self):  # Define function to drop an item
        number = simpledialog.askinteger("Drop Item", "Enter the number of the item to drop:")  # Prompt user to enter item number
        if number is None or number < 1 or number > len(self.inventory):  # Check if number is invalid
            messagebox.showerror("Error", "Invalid item number.")  # Show error message
        else:  # If number is valid
            item = self.inventory.pop(number - 1)  # Remove item from inventory
            messagebox.showinfo("Item Dropped", f"{item} was dropped.")  # Show confirmation message
            self.show_inventory()  # Refresh inventory display

def main():  # Define main function
    root = tk.Tk()  # Create the main Tkinter window
    app = InventoryApp(root)  # Create an instance of the InventoryApp class
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function
