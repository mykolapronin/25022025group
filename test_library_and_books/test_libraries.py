class TestLibrary:

    def test_library_name(self, library):
        assert library.library_name == 'The Library Of Congress'

    def test_library_list_of_books(self, library):
        assert library.list_of_books == []

    def test_add_book_in_library(self, library, book, another_book):
        library.add_book(book)
        library.add_book(another_book)
        assert book in library.list_of_books
        assert another_book in library.list_of_books

    def test_remove_book_from_library(self, library, book, another_book):
        library.remove_book(book)
        library.remove_book(another_book)
        assert book not in library.list_of_books
        assert another_book not in library.list_of_books
