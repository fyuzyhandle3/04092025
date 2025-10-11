class Book:
    def __init__(self, author, title, book_id ):
        self.author = author
        self.title = title
        self.book_id = book_id


    def __str__(self):
        return f"[{self.book_id}] {self.author} - «{self.title}»"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []


    def add_book(self, book: Book):
        """Add the book to the library"""
        self.books.append(book)
        print(f"Book {book.title} was added to the library «{self.name}».")


    def remove_book(self, book_id: int):
        """deliting book by id"""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book with id {book_id} eas deleted «{self.name}»")
                return
            print(f"Book with id {book_id} not found")

    def show_books(self):
        """output all of the book in server"""
        if not self.books:
            print('in the library this book not found')
        else:
            print(f"Book in the Library «{self.name}» not found")
            for book in self.books:
                print("-", book)



if __name__ == "__main__":
    library = Library("The Central Library")

    book1 = Book("Napoleon Hill", "Think and be rich", 1)
    book2 = Book("Donald Uolsh", "Conversation with God", 2)

    library.add_book(book1)
    library.add_book(book2)
    library.show_books()

    library.remove_book(1)
    library.show_books()