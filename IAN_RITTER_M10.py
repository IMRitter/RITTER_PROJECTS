#Name: (Ian Ritter)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 20 JULY 2024
#Project #: M10
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv

# Displaying the title of program
def display_title():
    print("Ian Ritter's Monthly Sales")
    print()

def display_menu():
    print("COMMAND MENU\n")
    print("monthly - View monthly sales")
    print("yearly  - View yearly summary")
    print("edit    - Edit sales for a month")
    print("exit    - Exit program")
    print()  # To add an extra space after the menu


def read_sales():
    sales = []  # Initialize an empty list for sales
    FILENAME = 'monthly_sales.csv'  # Name of the CSV file
    # Open, read, and close the CSV file
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)  # Append each row to sales list
    return sales  # Return the sales list


def main():
    display_title()  # Call display_title() to show the title
    display_menu()  # Call display_menu() to show the command menu
    sales = read_sales()  # Read sales data from CSV and assign to sales

    # Create a while loop to execute commands
    while True:
        command = input("Command: ")  # Get user input for command
        if command == "monthly":
            view_monthly_sales(sales)  # View monthly sales
        elif command == "yearly":
            view_yearly_summary(sales)  # View yearly summary
        elif command == "edit":
            edit(sales)  # Edit sales for a month
        elif command == "exit":
            break  # Exit the program
        else:
            print("Not a valid command. Please try again.\n")  # Invalid command
    print("Bye!")  # Print goodbye message

# Define view_monthly_sales(sales) function
def view_monthly_sales(sales):
    # Display monthly sales
    for row in sales:
        print(f"{row[0]} - {row[1]}")  # Print month and sales amount
    print()  # Add space

# Define view_yearly_summary(sales) function
def view_yearly_summary(sales):
    total = 0  # Initialize total sales
    # Calculate total sales
    for row in sales:
        amount = int(row[1])  # Get sales amount
        total += amount  # Add to total
    count = len(sales)  # Get number of months
    average = total / count  # Calculate average sales
    average = round(average, 2)  # Round average to two decimal places
    # Display yearly total and monthly average
    print("Yearly total:    ", total)
    print("Monthly average: ", average)
    print()  # Add space

# Define edit(sales) function
def edit(sales):
    names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # List of month names
    name = input("Three-letter month: ").title()  # Get user input for month
    if name not in names:
        print("Invalid three-letter month.")  # Invalid month
        return
    index = names.index(name)  # Get index of the month
    amount = int(input("Sales amount: "))  # Get sales amount
    month = []  # Initialize month list
    month.append(name)  # Add month name to list
    month.append(str(amount))  # Add sales amount to list
    sales[index] = month  # Update sales list
    write_sales(sales)  # Write updated sales to CSV
    print(f"Sales amount for {month[0]} was modified.")  # Confirm modification
    print()  # Add space

# Define write_sales(sales) function
def write_sales(sales):
    FILENAME = 'monthly_sales.csv'  # Name of the CSV file
    # Open, write, and close the CSV file
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales)  # Write sales data to file

# Add entry point to call main() function
if __name__ == "__main__":
    main()

