# ask 2: Bookstore Inventory System (Using Git Branches)

# Goal: Build an app to manage books in a store.

# Features:

# - Book class: title, author, price, stock

# - Use inventory.py for inventory logic

# - Save inventory in books.json

# - Use math module for rounding prices

# - Use Git: Create and merge feature branches

#  * git checkout -b feature-search

#  * git merge feature-search
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'book.json')

class Book:
    def __init__(self, title, author,price,stock):
        self.title = title
        self.author = author
        self.price = round(float(price),2)
        self.stock = int(stock)
    
    def to_dict(self):
        return{
            "title": self.title,
            "author":self.author,
            "price": self.price,
            "stock": self.stock
        } 
        
def load_inventory():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return[]

def save_inventory(books):
    with open(DATA_FILE, 'w') as f:
        return json.dump(books, f, indent=4)

def addbook():
    title = input("title: ")
    author =input("Author: ")
    price =input("Price: ")
    stock =input("stock: ")
    
    
    book = Book(title, author, price, stock)
    books =load_inventory()
    books.append(book.to_dict())
    save_inventory(books)
    print("Book Saved successfully")
    
def view_inventory():
    books = load_inventory()
    if not books:
        print("No book Available")
    for book in books:
        print(f"{books['title']} by ${books['author']} - {books['price']} (Stock: {books['stock']})")
        
def search():
    query = input("Input text to search: ").lower()
    found =[]
    books = load_inventory()
    for book in books:
        if query in book['title'].lower() or query in book['author'].lower():
            found.append(book)
            
    if found:
        print("Search Results:")
        for book in found:
            print(f"{book['title']} by {book['author']} - ₦{book['price']} (Stock: {book['stock']})")


def menu():
    while True:
        print("-----Inventory App----")
        print("1. Add Book")
        print("2. View Inventory")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':   
            addbook()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            search()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
        
        