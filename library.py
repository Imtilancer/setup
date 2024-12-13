import os
import json
from datetime import datetime, timedelta

class LibraryManagement:
    def _init_(self, books_file="books.json", lend_file="lends.json"):
        self.books_file = books_file
        self.lend_file = lend_file
        self.books = self.load_books()
        self.lends = self.load_lends()

    def load_books(self):
        """Loads books data from a JSON file."""
        if os.path.exists(self.books_file):
            with open(self.books_file, "r") as file:
                return json.load(file)
        return {}

    def save_books(self):
        """Saves books data to a JSON file."""
        with open(self.books_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def load_lends(self):
        """Loads lend data from a JSON file."""
        if os.path.exists(self.lend_file):
            with open(self.lend_file, "r") as file:
                return json.load(file)
        return []

    def save_lends(self):
        """Saves lend data to a JSON file."""
        with open(self.lend_file, "w") as file:
            json.dump(self.lends, file, indent=4)

    def add_book(self, title, quantity):
        """Adds a new book or updates quantity if the book already exists."""
        if title in self.books:
            self.books[title]["quantity"] += quantity
        else:
            self.books[title] = {"quantity": quantity}
        self.save_books()
        print(f"Added {quantity} copies of '{title}'.")

    def view_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("No books available in the library.")
            return

        print("\n--- Library Books ---")
        for title, info in self.books.items():
            print(f"Title: {title}, Quantity: {info['quantity']}")

    def lend_book(self, borrower_name, phone, title):
        """Allows a user to borrow a book."""
        if title not in self.books:
            print(f"The book '{title}' is not available in the library.")
            return

        if self.books[title]["quantity"] == 0:
            print("There are not enough books available to lend.")
            return

        return_date = datetime.now() + timedelta(days=14)
        self.lends.append({
            "borrower_name": borrower_name,
            "phone": phone,
            "title": title,
            "return_date": return_date.strftime("%Y-%m-%d")
        })

        self.books[title]["quantity"] -= 1
        self.save_books()
        self.save_lends()
        print(f"'{title}' has been lent to {borrower_name}. Return due date: {return_date.strftime('%Y-%m-%d')}.")

    def return_book(self, borrower_name, title):
        """Allows a borrower to return a book."""
        lend_info = next((lend for lend in self.lends if lend["borrower_name"] == borrower_name and lend["title"] == title), None)
        if not lend_info:
            print(f"No lend record found for {borrower_name} with the book '{title}'.")
            return

        self.lends.remove(lend_info)
        self.books[title]["quantity"] += 1
        self.save_books()
        self.save_lends()
        print(f"'{title}' has been returned by {borrower_name}.")

    def view_lends(self):
        """Displays all current lend records."""
        if not self.lends:
            print("No books are currently lent out.")
            return

        print("\n--- Lend Records ---")
        for lend in self.lends:
            print(f"Borrower: {lend['borrower_name']}, Phone: {lend['phone']}, Title: {lend['title']}, Return Due: {lend['return_date']}")

def main():
    library = LibraryManagement()

    while True:
        print("\n--- Library Management Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. View Lend Records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            try:
                quantity = int(input("Enter quantity: ").strip())
                library.add_book(title, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            borrower_name = input("Enter borrower's name: ").strip()
            phone = input("Enter borrower's phone number: ").strip()
            title = input("Enter book title: ").strip()
            library.lend_book(borrower_name, phone, title)

        elif choice == "4":
            borrower_name = input("Enter borrower's name: ").strip()
            title = input("Enter book title: ").strip()
            library.return_book(borrower_name, title)

        elif choice == "5":
            library.view_lends()

        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()