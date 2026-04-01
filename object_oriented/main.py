

class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"

book_1 = Book("100 años de soledad", "Gabriel Garcia Marquez", "9788497592208", True)
book_2 = Book("La voragine", "Jose Eustasio Rivera", "9781520760933", False)
book_3 = Book("Sunrise on the reaping", "Suzanne Collins", "9781546171461", True)
book_4 = Book("A clash of kings", "George R.R. Martin", "9780553381696", True)

catalog = [book_1, book_2, book_3, book_4]

for book in catalog:
    print(book)