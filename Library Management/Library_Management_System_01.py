class Book:
    # Class attribute to keep track of the total number of books
    total_books = 0
    
    # Initialize a book object with title, author, and availability status
    def __init__(self, title, author, available=True):
        self._title = title       # Title of the book (private attribute)
        self._author = author     # Author of the book (private attribute)
        self._available = available  # Availability status (private attribute)
        Book.total_books += 1     # Increment the total number of books

    # Getter method for the title
    @property
    def title(self):
        return self._title

    # Setter method for the title (if you want to modify the title)
    @title.setter
    def title(self, new_title):
        self._title = new_title

    # Getter method for the author
    @property
    def author(self):
        return self._author

    # Setter method for the author
    @author.setter
    def author(self, new_author):
        self._author = new_author

    # Class property to check availability of the book
    @property
    def available(self):
        return self._available

    # Setter method for updating availability status (borrow/return)
    @available.setter
    def available(self, status):
        self._available = status

    # Class method to get the total number of books
    @classmethod
    def get_total_books(cls):
        return cls.total_books

    # Method to borrow the book (if available)
    def borrow_book(self):
        if self._available:
            self._available = False
            print(f"You've borrowed the book: {self._title}")
        else:
            print(f"Sorry, the book '{self._title}' is currently unavailable.")

    # Method to return the book
    def return_book(self):
        if not self._available:
            self._available = True
            print(f"Thank you for returning the book: {self._title}")
        else:
            print(f"The book '{self._title}' was not borrowed.")

# Demonstrating the Library Management System

# Creating some book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Display total number of books
print(f"Total number of books: {Book.get_total_books()}\n")

# Borrow a book
book1.borrow_book()
book1.borrow_book()  # Try borrowing again (should be unavailable)

# Return a book
book1.return_book()
book1.return_book()  # Try returning again (should not be borrowed)

# Check availability using the class property
print(f"\nIs '{book1.title}' available? {book1.available}")

# Modifying book title using setter
print(f"\nOld Title: {book2.title}")
book2.title = "Go Set a Watchman"  # Changing the title
print(f"New Title: {book2.title}")

# Checking availability for a different book
print(f"\nIs '{book3.title}' available? {book3.available}")
book3.borrow_book()  # Borrowing it

# Display total number of books again
print(f"\nTotal number of books in the library: {Book.get_total_books()}")
