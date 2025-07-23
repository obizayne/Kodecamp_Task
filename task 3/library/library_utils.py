# library_utils.py

import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'books.json')

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'available': self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data['title'], data['author'], data['available'])

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You have borrowed '{book.title}'.")
                return
        print("Book not available or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You have returned '{book.title}'.")
                return
        print("Book not found or wasn't borrowed.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"'{book.title}' by {book.author} - {status}")

    def save_to_file(self):
        with open(DATA_FILE, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)
        print("Library saved to file.")

    def load_from_file(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
            print("Library loaded from file.")
