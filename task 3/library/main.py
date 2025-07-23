# main.py

from library_utils import Library

def main():
    library = Library()
    library.load_from_file()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == '2':
            title = input("Enter title of book to borrow: ")
            library.borrow_book(title)

        elif choice == '3':
            title = input("Enter title of book to return: ")
            library.return_book(title)

        elif choice == '4':
            library.view_books()

        elif choice == '5':
            library.save_to_file()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
