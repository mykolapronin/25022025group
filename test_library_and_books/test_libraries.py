class TestLibrary:

    def test_library_name(self, library):
        assert library.library_name == "The Library Of Congress"

    def test_add_book_to_library(self, library, book):
        if book.inn is not library.list_of_books:
            library.list_of_books.append(book.inn)

    def test_remove_book_from_library(self, library, book):
        if book.inn in library.list_of_books:
            library.list_of_books.remove(book.inn)
