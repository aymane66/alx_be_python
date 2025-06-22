class Book:
    def __init__(self, title, author):
        self.title = title
        self.author= author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

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
        for b in self.books:
            print(f"Book: {b.title} by {b.author}")
        for eb in self.ebooks:
            print(f"EBook: {eb.title} by {eb.author}, File size: {eb.file_size}KB")
        for pb in self.print_books:
            print(f"PrintBook: {pb.title} by {pb.author}, Page count: {pb.page_count}")


