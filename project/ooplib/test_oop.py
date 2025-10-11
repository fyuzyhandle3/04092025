import pytest
from hw290925 import Book, Library


@pytest.fixture
def sample_books():
    return [
        Book("Napoleon Hill", "Think and be rich", 1),
        Book("Donald Walsh", "Conversation with God", 2),
        Book("Joanne Rowling", "Harry Potter", 3)
    ]


@pytest.fixture
def test_library(sample_books):
    lib = Library("test Library")
    for book in sample_books:
        lib.add_book(book)
    return lib


class TestBook:
    @pytest.mark.parametrize(
        "author, title, book_id, expected_str",
        [
            ("Napoleon Hill", "Think and be rich", 1, "[1] Napoleon Hill - «Think and be rich»"),
            ("Donald Walsh", "Conversation with God", 2, "[2] Donald Walsh - «Conversation with God»"),
            ("Joanne Rowling", "Harry Potter", 3, "[3] Joanne Rowling - «Harry Potter»"),
        ]
    )
    def test_book_str(self, author, title, book_id, expected_str):
        book = Book(author, title, book_id)
        assert str(book) == expected_str


class TestLibrary:
    def test_add_book(self, test_library):
        new_book = Book("Arthur Conan Doyle", "Sherlock Holmes", 4)
        test_library.add_book(new_book)
        assert new_book in test_library.books
        assert len(test_library.books) == 4

    @pytest.mark.parametrize("book_id_to_remove", [1, 2])
    def test_remove_book_existing(self, test_library, book_id_to_remove):
        test_library.remove_book(book_id_to_remove)
        ids = [book.book_id for book in test_library.books]
        assert book_id_to_remove not in ids

    def test_remove_book_not_existing(self, test_library, capsys):
        test_library.remove_book(1000)
        captured = capsys.readouterr()
        assert "not found" in captured.out.lower()

    def test_show_books_empty(self, capsys):
        lib = Library("Empty library")
        lib.show_books()
        captured = capsys.readouterr()
        assert "not found" in captured.out.lower()
