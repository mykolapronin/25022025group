class TestBook:

    def test_book_title(self, book):
        assert book.book_title == "The Greatest Party"

    def test_books_author(self, book):
        assert book.author_name == "Nikola"


class TestAnotherBook:
    def test_another_book_title(self, another_book):
        assert another_book.book_title == "After party"

    def test_another_book_author(self, another_book):
        assert another_book.author_name == "Gabe"
