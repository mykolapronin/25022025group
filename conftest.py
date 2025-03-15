import pytest

from library_models import Book, Library


@pytest.fixture(scope="session")
def book() -> Book:
    return Book(book_title="The Greatest Party", author_name="Nikola")


@pytest.fixture(scope="session")
def another_book() -> Book:
    return Book(book_title="After party", author_name="Gabe")


@pytest.fixture(scope="session")
def library() -> Library:
    return Library("The Library Of Congress")
