class Library:
    def __init__(self, book_list, librarian_name):
        self.book_list = book_list
        self.librarian_name = librarian_name
        self.lend_record = {book: None for book in book_list}

    def display_book(self):
        print(f"Books available in {self.librarian_name}:")
        for book in self.book_list:
            print(book)
        print("_____________________________")
        print("Lent Books:")
        empty_borrower_found = True
        for book, borrower in self.lend_record.items():
            if borrower:
                print(f"Book: {book} | Borrower: {borrower}")
                empty_borrower_found = False
        if empty_borrower_found:
            print("None")

    def add_book(self):
        book = input("Enter book's name: ").capitalize()
        if book in self.book_list or book in self.lend_record:
            print("Book already exists in the library.")
        else:
            self.book_list.append(book)
            self.lend_record[book] = None
            print(f"Book '{book}' added successfully.")

    def lend_book(self):
        book = input("Enter book name: ").capitalize()
        if book in self.lend_record and self.lend_record[book] is not None:
            print(f"Book '{book}' is not available. It's taken by {self.lend_record[book]}")
        else:
            if book in self.book_list:
                name = input("Enter your name: ")
                self.book_list.remove(book)
                self.lend_record[book] = name
                print(f"Book '{book}' lent to {name}.")
            else:
                print(f"Book '{book}' not found in the library.")

    def return_book(self):
        book = input("Enter book name: ").capitalize()
        if book in self.lend_record and self.lend_record[book] is not None:
            self.book_list.append(book)
            self.lend_record[book] = None
            print(f"Book '{book}' returned successfully.")
        else:
            print(f"Book '{book}' is not currently borrowed.")

if __name__ == '__main__':
    book_list = ['English', 'Nepali', 'Science', 'Maths']
    venom_library = Library(book_list, "Venom's Library")

    while True:
        print("\nD: Display, A: Add book, L: Lend book, R: Return book, Q: Exit/Quit")
        user = input()
        if user.upper() == "Q":
            break
        elif user.lower() in ("d", "display"):
            venom_library.display_book()
        elif user.lower() in ("a", "add"):
            venom_library.add_book()
        elif user.lower() in ("l", "lend"):
            venom_library.lend_book()
        elif user.lower() in ("r", "return"):
            venom_library.return_book()
        else:
            print("Invalid input. Please try again.")
