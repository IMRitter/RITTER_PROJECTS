#!/usr/bin/env python3

# display a welcome message
print("Ian Ritter's Miles Per Gallon Application")
print()

another_trip = "y" #create variable for while condition
#while loop to ask user for multiple trips
while another_trip =="y":
    # get input from the user
    miles_driven    = float(input("Enter miles driven:         "))
    gallons_used    = float(input("Enter gallons of gas used:  "))
    #retrieve cost per gallon from the user via input
    cost_per_gallon  = float(input("Enter the cost per gallon:  "))

    print() #added a space

#boolean expressions to check whether the user input is valid
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero, Please try again.")
    else:
        # calculate the mpg, total gas cost, cost per mile
        mpg = round((miles_driven / gallons_used), 2)
        total_gas_cost = round(gallons_used * cost_per_gallon, 2)
        cost_per_gallon = round(total_gas_cost / miles_driven,2)

        #Display the mpg, total gas cost, and cost per mile
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_gallon)


    #Print blank lines and prompt the user for another trip
    print()
    another_trip = input("Go on another trip? (y/n)")
    print()


print("Bye")



