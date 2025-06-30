
# main.py

from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)         # Should call __str__
    print(repr(my_book))   # Should call __repr__

    del my_book            # Should call __del__

if __name__ == "__main__":
    main()



