import uuid


class Book:
    def __init__(self, author_name: str, book_title: str):
        self.book_title: str = book_title
        self.author_name: str = author_name
        self.inn: uuid.UUID = uuid.uuid4()

    def __str__(self):
        return (
            f"<Book {self.book_title} and the authr {self.author_name},"
            f"the id of this book is {self.inn}>"
        )


class Library:
    def __init__(self, library_name: str, list_of_books: list):
        self.library_name = library_name
        self.list_of_books = list_of_books

    def add_book(self, book=Book):
        self.list_of_books.append(book)

    def remove_book(self, book=Book):
        for book.inn in self.list_of_books:
            self.list_of_books.remove(book)
