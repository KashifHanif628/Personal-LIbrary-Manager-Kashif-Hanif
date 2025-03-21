import json # its a Module & use for save & load data.
import os # its use for file handling ans system operation.
import datetime as datetime


data_file = "library.txt"

# to check the load library data
def load_library(): # initialize a fundtion here with the name of load_library 
    if os.path.exists(data_file): # implement the condition here & it will check above data_file (library.txt) available or not ? if yes,
        with open(data_file, "r") as file: # then open the data_file in read mode (r used here as read)
            return json.load(file) # and save or load the file in json.load
    return []


# save library
def save_library(library): # initialize a fundtion here with the name of save_library and passed the parameter of library & its using here to send the data in funtion.
    # i.e. when we call the above funtion so its need a list or dictionary to passed/write the data which is our library data.
    with open(data_file, "w") as file: # then open the (library.txt) data_file in write mode (w used here as write)
        return json.dump(library, file) # and convert the library data in json format & will save in the file.
    

# funtion to add the book
def add_book(library):
    title = input("Please enter the title of the book: ")
    author = input("Please enter author of the book: ")
    year = input("Please enter the publication year of the book: ")
    genre = input("Please enter the genre of the book: ")
    read = input("Have you read the book ? (yes/no): ").lower() == "yes"
    date_input = input("Please enter the date & time of adding the book (YYYY-MM-DD HH:MM:SS): ")
    try:
        added_date = datetime.datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S").strftime("%y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format! Using current date & time instead.")
        added_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

# created dictionary / list
    new_book = {
        "title" : title,
        "author" : author,
        "year" : year,
        "genre" : genre,
        "read" : read,
        "added_date" : added_date
    }

    library.append(new_book)# append used here to add the new book
    save_library(library)
    print(f"Book {title} added successfully.")


# function to remove book
def remove_book(library):
    title = input("Please enter the title of book, which is you want to remove or deleat from the library.")
    initial_length = len(library) # it shows our total library books in qunatity i.e how many books are in library. 
    library = [book for book in library if book["title"].lower() != title]
    if len(library) < initial_length: # when any book removed from the library
        save_library(library) # then save it again remaining book of library.
        print(f"Book {title} removed successfully.") # print a message that book have removed successfully.
    else: 
        print(f"Book {title} not found in the library.") # if title of book not matching from the library then print a message of not found.


# function to search the book in library.
def search_library(library):
    search_by = input("Search by title or author: ").strip().lower()  # ask for user input to search the book by title or author
    search_term = input(f"Please enter the {search_by}: ").strip().lower()  # used search_term to find the book by title or author

    # if user find the book by title in ibrary
    if search_by == "title":
        results = [book for book in library if search_term in book["title"].lower()]
    # if user find the book by author
    elif search_by == "author":
        results = [book for book in library if search_term in book["author"].lower()]
    # if invalid name provided by the user then print the below message.
    else:
        print("Invalid search option! Please enter 'title' or 'author'.")
        return

# used for loop to search the multiple books with read or unread.
    if results:
        for book in results:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No book found in result by matching '{search_term}' in the {search_by} field.")

# funtion to dispaly all the book display.
def display_all_books(library): # initialize the function 
    if library: # apply the condition here
        for book in library: # used for loop here to display the all books Read or Unread
            status = "Read" if book ["read"] else "Unread"  
            print(f"{book["title"]} by {book["author"]} - {book["year"]} - {book["genre"]} - {status}")
    else:
        print("The Library is empty, there is no book to display.") # other-wise print this message.


# funtion to display statistics.
def display_statistics(library): # initialize the function
    total_books = len(library) # if library length is equal to total books of library. 
    read_books = len([book for book in library if book["read"]]) # then count the read books length in library. 
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0 # & also count the percentage of read books of library.

    print(f"Total books: {total_books}") # print the message of total books of library.
    print(f"Percentage read: {percentage_read:.2f}%")# also print the message of percentage read books & .2f method used for after .2 digits.


# main funtion 
def main():
    library = load_library()
    while True: # used infinite loop to continue/display the programme/menu till the user exite.
        print("Welcom to M.Kashif Hanif Library Manager")
        print("Menu")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search the Library")
        print("4. Display all Books")
        print("5. Display Statistics")
        print("6. Exist")

        choise = input("Please enter the options, which one would you like to perform.")
        if choise == '1':
            add_book(library)
        elif choise == '2':
            remove_book(library)
        elif choise == '3':
            search_library(library)
        elif choise == '4':
            display_all_books(library)
        elif choise == '5':
            display_statistics(library)
        elif choise == '6':
            print("Thanks for visiting the Kashif Hanif Personal Library Collection, Good-Bye! and have a nice day.")
            break
        else: # if user select 7 option which is not exist in library then print the below message.
            print("Invalid choise! Please select the correct option again.")

if __name__ == '__main__':
    main()

    