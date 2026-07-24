class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print(title, "added successfully.")

    def display_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            if book.available:
                print(book.title, "- Available")
            else:
                print(book.title, "- Borrowed")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("You borrowed:", title)
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print("You returned:", title)
                return
        print("Book not found or already returned.")


# Main Program
library = Library()

library.add_book("Python")
library.add_book("Java")
library.add_book("C++")

library.display_books()

library.borrow_book("Python")
library.display_books()

library.return_book("Python")
library.display_books()

'''
OUTPUT:

Python added successfully.
Java added successfully.
C++ added successfully.

Books in Library:
Python - Available
Java - Available
C++ - Available

You borrowed: Python

Books in Library:
Python - Borrowed
Java - Available
C++ - Available

You returned: Python

Books in Library:
Python - Available
Java - Available
C++ - Available

'''
