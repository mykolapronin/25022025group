import pytest
from library_models import Book, Library


@pytest.fixture(scope="session")
def book() -> Book:
    return Book(book_title='The Greatest Party', author_name='Unknoasdasdwn')


@pytest.fixture(scope="session")
def another_book() -> Book:
    return Book(book_title='asdfasf', author_name='adsdasdas')


@pytest.fixture(scope="session")
def library() -> Library:
    return Library("The Library Of Congress", [])
