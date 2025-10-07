# Library management system
import os
import yaml

LIST_FILE = "list.yaml"


def load_books():
    if os.path.exists(LIST_FILE):
        with open(LIST_FILE, "r") as file:
            return yaml.safe_load(file)
    else:
        # Default book data if YAML doesn't exist yet
        return {
            "books": [
                {
                    "name": "1984",
                    "author": "George Orwell",
                    "pages": 328,
                    "publish_date": 1949,
                    "available": True,
                },
                {
                    "name": "The Great Gatsby",
                    "author": "F. Scott Fitzgerald",
                    "pages": 180,
                    "publish_date": 1925,
                    "available": True,
                },
                {
                    "name": "To Kill a Mockingbird",
                    "author": "Harper Lee",
                    "pages": 281,
                    "publish_date": 1960,
                    "available": True,
                },
            ]
        }


def save_books(data):
    with open(LIST_FILE, "w") as file:
        yaml.safe_dump(data, file)


def view_books(books):
    print("\n--- List Of Books --- ")
    for i, book in enumerate(books["books"], 1):
        status = "Available" if book["available"] else "Borrowed"
        print(
            f"{i}. {book['name']} by {book['author']} ({book['pages']} pages, {book['publish_date']}) - {status}"
        )
    print()


def borrow_books(books):
    view_books(books)
    choice = int(input("Enter the number of the book to borrow >> "))
    selected_book = books["books"][choice - 1]

    if selected_book["available"]:
        selected_book["available"] = False
        print(f"You have borrowed '{selected_book['name']}'.")
        save_books(books)
    else:
        print(f"\n'{selected_book['name']}' is unavailable right now\n")


def return_books(books):
    view_books(books)
    choice = int(input("Enter the number of the book to return >> "))
    selected_book = books["books"][choice - 1]

    if not selected_book["available"]:
        selected_book["available"] = True
        print(f"You have successfully return '{selected_book['name']}'.")
        save_books(books)
    else:
        print(f"The {selected_book['name']} was not borrowed")


def main():
    books = load_books()

    while True:
        print("Welcome to Janie Library")
        print("1. View Books")
        print("2. Borrow Books")
        print("3. Return Books")
        print("4. Exit")

        choice = int(input("Select your choice >> "))

        if choice == 1:
            view_books(books)
        elif choice == 2:
            borrow_books(books)
        elif choice == 3:
            return_books(books)
        elif choice == 4:
            print("Thank you and come again!!")
            break
        else:
            print("Invalid choice. Please select again")


if __name__ == "__main__":
    main()
