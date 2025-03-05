#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    # create new list variable to hold scores
    scores = [] 
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            try:
                score = int(score)
                if score >= 0 and score <= 100:
                    scores.append(score) 
                else:
                    print("Test score must be from 0 through 100. " +
                          "Score discarded. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid test score or 'x' to exit.")


def process_scores(scores):
    # sort the scores
    scores.sort()

    # Calculate total scores
    total = sum(scores)

    # find the number of scores
    num_scores = len(scores)

    # calculate average score
    average = total / num_scores if num_scores > 0 else 0

    # find the low score
    low_score = min(scores) if num_scores > 0 else 0

    # find the high score
    high_score = max(scores) if num_scores > 0 else 0

    # find the median score
    median = 0
    median_index = num_scores // 2
    if num_scores % 2 == 1:
        median = scores[median_index]
    elif num_scores > 0:
        middle_1 = scores[median_index]
        middle_2 = scores[median_index-1]
        median = (middle_1 + middle_2) / 2

    # format and display the result
    print()
    print("Score total:         ", total)
    print("Number of Scores:    ", num_scores)
    print("Average Score:       ", average)
    print("Low Score:           ", low_score)
    print("High Score:          ", high_score)
    print("Median:              ", median)


def main():
    display_welcome()
    # retrieve the list from the get_scores() function
    scores = get_scores()
    # retrieve and display the values for the provided list
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
