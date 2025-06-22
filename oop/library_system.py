# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def _str_(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def _str_(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def _str_(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

def main():
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    printbook = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    print(book1.display_info())
    print(ebook.display_info())
    print(printbook.display_info())

if __name__ == "__main__":
    main()

