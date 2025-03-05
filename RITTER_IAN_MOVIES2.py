# import modules for csv and sys, allows for interacting with csv files
# sys enables us to use sys functions like exit()
import csv
import sys

# global constant for file name
FILENAME = "movies_test.csv"

#exit proram function, print message


def exit_program():
    # print a message to exit and then exit using the sys.exit() method
    print("Terminating program.")
    # exit the application
    sys.exit()

# open and interact with csv file


def read_movies():
    # try to open the file and read it 
    try:
        # declare list for movies
        movies = []        
        # open the file using the reader object
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            # add file contents to the movies list
            for row in reader:
                movies.append(row)
        return movies
    # exception for file not found
    except FileNotFoundError as e:
        # print(f"Could not find {FILENAME} file. ")
        # exit_program()
        return movies
    # all other exceptions    
    except Exception as e:
        # print out the exception type and exit the program
        print(type(e), e)
        exit_program()

# open file and write to it


def write_movies(movies):
    #try to open the file for writin
    try:
        # open the file using a writer object
        with open(FILENAME, "w", newline="") as file:
            ## raise BlockingIOError("Test the OSError exeception.")
            writer = csv.writer(file)
            # write the passed in movies parameter to the file
            writer.writerows(movies)
    # exception for OS-related errors
    except OSError as e:
        print(type(e), e)
        exit_program()
    # exception for catching all exceptions
    except Exception as e:
        # print out the exception type and exit the program
        print(type(e), e)
        exit_program

# iterate through movies parameter and list them out


def list_movies(movies):
    # for loop to iterate through the movies list
    for i, movie in enumerate(movies, start=1):
        # print each movie row
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()

# add a new movie to the file

    
def add_movie(movies):
    # retrieve user's input for new movie details
    name = input("Name: ")
    while True:
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid year/ Please try again.")
            continue
        if year <= 0:
            print("Year must be greater than zero. Please try again.")
            continue
        else:
            break
    # append movie details to movies list
    movie = [name, year]
    movies.append(movie)
    # write the movies to the file
    write_movies(movies)
    # print what was added
    print(f"{name} was added.\n")

    # remove a movie from the file


def delete_movie(movies):
    # while loop to ask the user for a valid movie to delete
    while True:
        # try to check for valid number that identifies a movie
        try:
            number = int(input("Number: "))
        # catching value errors
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        # further validation for range
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    # remove the movie from the movies list
    movie = movies.pop(number - 1)
    # write the modified list to the file
    write_movies(movies)
    # print out what movie was deleted
    print(f"{movie[0]} was deleted.\n")

# display general information about the program


def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print() 

# main code that will execute
   

def main():
    # show the menu
    display_menu()
    # read the movies from the file
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
