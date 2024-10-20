class Book:
    # class attribute to keep track total number of the books
    total_books: int = 0
    # initialize a book object with book title, author, and availability of the book

    def __init__(self, title, author, available = True):
        self._title = title # Title of the book attribute (private attribute)
        self._author = author # Author of the book (Private attribute)
        self._available = available # Availability status (private attribute)
        Book.total_books += 1 # Increment the total number of books
    # Getter method for title
    @property
    def title(self):
        return self._title
    # setter for title (if you want to modify the title)
    @title.setter
    def title(self, new_title):
        self._ttile = new_title
    # getter method for author
    @property
    def author(self):
        return self._author
    # Setter Method for author (if you want to correct the name of auth because it may be missespell during first entry.)
    @author.setter
    def author (self, new_author):
        self._author = new_author
    # Class Property to check availability of the book
    @property
    def available(self):
        return self._available
    # setter method for updating availabilty status
    @available.setter
    def available(self, status):
        self._available = status
        # class method to get total number of books
    @classmethod
    def total_books(cls):
        return cls.total_books
    # Method to borrow the book if available
    def borrow_book(self):
        if self.available:
            self._available = False
            print(f"You have borrowed the book: {self._title}")
        else:
            print(f" Sorry: The book {self._title} is currently unavailable.")
    
    # Method to return book
    def return_book(self):
        if self.available:
            self._available = True
            print(f"Thank You for return book {self._title}")
        else:
            print(f"The book {self._title} was not borrowed.")
# Demonstrating the library management system
book1 = Book("1984", "George Orwell")
book2 = Book("2016", "Why Nation Fails")
book3 = Book("Pakistan Beyond the crisis State", "Maleha Lodhi")

print(f"Total number of books: {Book.total_books()}\n")

#Borrow a Book
book1.borrow_book()
book1.borrow_book() # try borrow again will not be available

# return a book
book1.return_book()
book1.return_book() # returning book again (should not be borrowed.)

# Check availabilty using class property
print(f"\nIs {book1.title} available? {book1.available}")

# modify book title using setter
print(f"\nOld Title: {book2.title}")

book2.title = "How Democracy Die?" # Changing the title of the book

print(f"'nNew Title: {book2.title}")

# Checking availabilty for different book
print(f"\nIs {book3.title} available? {book3.available}")
book3.borrow_book() # Borrowing book

# Display Total Number of Books Again
print(f"\nTotal Number of Books in the library: {Book.total_books()}")
        



