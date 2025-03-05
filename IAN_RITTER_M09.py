#Name: IAN RITTER
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 13 JULY 2024
#Project #: M09
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

def display_title(): # Define function to display title
    print("Ian Ritter's Wizard Inventory Game") # Title of program
    print()

def display_menu():  # Define function to display the command menu
    print("COMMAND MENU\n")  # Print command menu title
    print("show - Show all items")  # Print command to show items
    print("grab - Grab an item")  # Print command to grab an item
    print("edit - Edit an item")  # Print command to edit an item
    print("drop - Drop an item")  # Print command to drop an item
    print("exit - Exit program")  # Print command to exit program
    print()  # Print a blank line for spacing

def show(inventory):  # Define function to show inventory items
    print("Inventory:")  # Print inventory title
    for number, item in enumerate(inventory, start=1):  # Loop through inventory with item numbers starting from 1
        print(f"{number}. {item}")  # Print item number and name
    print()  # Print a blank line for spacing

def grab_item(inventory):  # Define function to grab an item
    if len(inventory) >= 4:  # Check if inventory has 4 or more items
        print("You can't carry any more items. Drop something first.\n")  # Print message if inventory is full
    else:  # If inventory has less than 4 items
        item = input("Enter the name of the item to grab: ")  # Prompt user to enter item name
        inventory.append(item)  # Add item to inventory
        print(f"{item} was added.\n")  # Print confirmation that item was added

def edit_item(inventory):  # Define function to edit an item
    number = int(input("Enter the number of the item to edit: "))  # Prompt user to enter item number
    if number < 1 or number > len(inventory):  # Check if entered number is valid
        print("Invalid item number.\n")  # Print error message for invalid number
    else:  # If number is valid
        item = input("Enter the new name of the item: ")  # Prompt user to enter new item name
        inventory[number - 1] = item  # Update item in inventory
        print(f"Item number {number} was updated.\n")  # Print confirmation that item was updated

def drop_item(inventory):  # Define function to drop an item
    number = int(input("Enter the number of the item to drop: "))  # Prompt user to enter item number
    if number < 1 or number > len(inventory):  # Check if entered number is valid
        print("Invalid item number.\n")  # Print error message for invalid number
    else:  # If number is valid
        item = inventory.pop(number - 1)  # Remove item from inventory
        print(f"{item} was dropped.\n")  # Print confirmation that item was dropped

def main():  # Define main function
    display_title()  # Call function to display title
    display_menu()  # Call function to display command menu
    
    inventory = ["staff", "wand", "potion"]  # Initialize inventory with default items
    
    while True:  # Start infinite loop
        command = input("Command: ")  # Prompt user to enter a command
        if command == "show":  # Check if command is "show"
            show(inventory)  # Call function to show inventory
        elif command == "grab":  # Check if command is "grab"
            grab_item(inventory)  # Call function to grab an item
        elif command == "edit":  # Check if command is "edit"
            edit_item(inventory)  # Call function to edit an item
        elif command == "drop":  # Check if command is "drop"
            drop_item(inventory)  # Call function to drop an item
        elif command == "exit":  # Check if command is "exit"
            break  # Exit loop and end program
        else:  # If command is invalid
            print("Not a valid command. Please try again.\n")  # Print error message for invalid command
    
    print("Bye!")  # Print goodbye message

if __name__ == "__main__":  # Check if script is being run directly
    main()  # Call main function
