class Book:
    def __init__(self, title, author):
        self.title = title
        self.author= author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:

    def __init__(self):
        self.books = []
        self.ebooks = []
        self.print_books = []

    def add_book(self, book):
        if isinstance(book, EBook):
            self.ebooks.append(book)
        elif isinstance(book, PrintBook):
            self.print_books.append(book)
        elif isinstance(book, Book):
            self.books.append(book)

    
    def list_books(self):
        for book in self.books:
            print(book)
        for ebook in self.ebooks:
            print(ebook)
        for print_book in self.print_books:
            print(print_book)

