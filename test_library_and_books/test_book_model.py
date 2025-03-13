class TestBook:
    def test_book(self, book):
        assert book.inn
        assert book.author_name
        assert book.book_title

    def test_inn_in_book(self, book, another_book):
        assert book.inn != another_book.inn


class TestBook2:
    def test_new_book(self, book):
        assert book.inn
        assert book.author_name
        assert book.book_title

    def test_inn_in_book(self, book, another_book):
        assert book.inn != another_book.inn
