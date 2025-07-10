#BSCIT-05-0836/2022
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title} has been borrowed."
        else:
            return f"{self.title} is already borrowed."

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not borrowed."

    def display_info(self):
        status = "Borrowed" if self.borrowed else "Available"
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Publication Year: {self.publication_year}\n"
            f"Status: {status}"
        )


class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        result = book.borrow_book()
        if "borrowed" in result.lower():
            self.borrowed_books.append(book)
        return result

    def return_book(self, book):
        result = book.return_book()
        if "returned" in result.lower() and book in self.borrowed_books:
            self.borrowed_books.remove(book)
        return result

    def display_info(self):
        books_list = "\n".join([book.title for book in self.borrowed_books]) if self.borrowed_books else "No books borrowed."
        return (
            f"Member ID: {self.member_id}\n"
            f"Name: {self.name}\n"
            f"Borrowed Books:\n{books_list}"
        )


#Sample Books
book1 = Book("Kigogo", "Ken Walibora", 2009)
book2 = Book("Blossoms of the Savannah", "Assumpta K Matei", 1990)
book3 = Book("The Pearl", "Daniel Mutubi", 2003)

available_books = [book1, book2, book3]

#Create a library member
member_id = int(input("Enter member ID: "))
member_name = input("Enter member name: ")
member = LibraryMember(member_id, member_name)

while True:
    print("\n--- Library Menu ---")
    print("1. View Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. View My Info")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\n--- Available Books ---")
        for i, book in enumerate(available_books):
            print(f"{i + 1}. {book.title} by {book.author} ({book.publication_year}) - {'Borrowed' if book.borrowed else 'Available'})")

    elif choice == '2':
        print("\n--- Choose a Book to Borrow ---")
        for i, book in enumerate(available_books):
            print(f"{i + 1}. {book.title}")
        selected_index = int(input("Enter the number of the book you want to borrow: ")) - 1
        if 0 <= selected_index < len(available_books):
            chosen_book = available_books[selected_index]
            print(member.borrow_book(chosen_book))
        else:
            print("Invalid selection.")

    elif choice == '3':
        if not member.borrowed_books:
            print("You have no books to return.")
        else:
            print("\n--- Choose a Book to Return ---")
            for i, book in enumerate(member.borrowed_books):
                print(f"{i + 1}. {book.title}")
            selected_index = int(input("Enter the number of the book you want to return: ")) - 1
            if 0 <= selected_index < len(member.borrowed_books):
                chosen_book = member.borrowed_books[selected_index]
                print(member.return_book(chosen_book))
            else:
                print("Invalid selection.")

    elif choice == '4':
        print("\n--- Member Information ---")
        print(member.display_info())

    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
