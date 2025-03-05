#!/usr/bin/env python3

# Import the random module
import random

# Function to display the title of the game
def display_title():
    print("Guess the number!")
    print()

# Function to get the upper limit for the range of numbers
def get_limit():
    limit = int(input("Enter the upper limit for the range of numbers: "))
    return limit

# Function to play the guessing game
def play_game(limit):
    # Generate a random number between 1 and the limit
    number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}\n")
    
    # Initialize the count of tries
    count = 0

    while True:
        # Get the user's guess
        guess = int(input("Your guess: "))
        # Increment the count for each guess
        count += 1
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        elif guess == number:
            print(f"You guessed it in {count} tries.\n")
            return

# Main function to run the game
def main():
    # Display the title of the game
    display_title()
    
    again = "y"
    while again.lower() == "y":
        # Get the upper limit for the range of numbers
        limit = get_limit()
        # Pass the limit to the play_game function
        play_game(limit)
        
        # Ask the user if they want to play again
        again = input("Play again? (y/n): ")
        print()
    # Print a goodbye message
    print("Bye!")

# If started as the main module, call the main function
if __name__ == "__main__":
    main()
