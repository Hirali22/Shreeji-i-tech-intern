# *Library Management mini system** (Books, issue/return)
class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available
        self.issued_to = None
    def issue(self, user):
        if self.available:
            self.available = False
            self.issued_to = user
            print(f"Book {self.title} issued to {user}")
        else:
            print(f"Book {self.title} is not available")
    def return_book(self):
        if not self.available:
            self.available = True
            self.issued_to = None
            print(f"Book {self.title} returned")
        else:
            print(f"Book {self.title} was not issued")
    def display(self):
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}")

book1 = Book(101, "Python Programming", "John Doe")
book1.display()
book1.issue("Alice")
book1.display()
book1.return_book()
book1.display()

    