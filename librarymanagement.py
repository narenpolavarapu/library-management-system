import time
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Availability:", "Available" if self.available else "Not Available")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None



library = Library()








while True:
    print("Select an operation to perform:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Find book")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Library Management System program exited.")
        print("-------------------")
        break

    if choice == '1':
        print("enter book id:")
        a=int(input(""))
        print("enter book name:")
        b=input("")
        print("enter author name:")
        c=input("")
        book1 = Book(a,b,c)
        library.add_book(book1)
        library.display_books()
        print("-------------------")
        time.sleep(1)
    elif choice == '2':
        print("enter book id to remove:")
        a=int(input(""))
        library.remove_book(a)
        library.display_books()
        print("-------------------")
        time.sleep(1)
    elif choice == '3':
        library.display_books()
        print("-------------------")
        time.sleep(1)
    elif choice == '4':
        print("enter book name to find:")
        a=input("")
        book = library.find_book(a)
        if book:
            print("\nBook Found:")
            book.display_info()
        else:
            print("\nBook not found.")

        print("-------------------")
        time.sleep(1)
    else:
        print("input is out of range! try 1-5")
        print("-------------------")
        time.sleep(1)
