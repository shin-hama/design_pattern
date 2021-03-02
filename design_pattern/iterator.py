""" Iterator Pattern
数え上げを行うインターフェースを作成することで、数える対象の実装とイテレートの実装を
分離する。
"""
from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def next(self) -> object:
        raise NotImplementedError


class ReverseIterator(ABC):
    @abstractmethod
    def has_previous(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def previous(self) -> object:
        raise NotImplementedError


class Aggregate(ABC):
    @abstractmethod
    def iterator(self) -> Iterator:
        raise NotImplementedError


class Book(object):
    def __init__(self, name: str):
        self._name: str = name

    def get_name(self) -> str:
        return self._name


class BookShelf(Aggregate):
    def __init__(self):
        self.books: list[Book] = []
        self.index: int = 0

    def get_book_at(self, index: int) -> Book:
        return self.books[index]

    def append_book(self, book: Book) -> None:
        self.books.append(book)

    def get_length(self) -> int:
        return len(self.books)

    def iterator(self) -> Iterator:
        return BookShelfIterator(self)

    def reverse_iterator(self) -> ReverseIterator:
        return BookShelfReverseIterator(self)


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf: BookShelf):
        self.book_shelf: BookShelf = book_shelf
        self.index: int = 0

    def has_next(self) -> bool:
        if self.index < self.book_shelf.get_length():
            return True
        else:
            return False

    def next(self) -> object:
        """ Get current book and move to next
        """
        book: Book = self.book_shelf.get_book_at(self.index)
        self.index += 1
        return book


class BookShelfReverseIterator(ReverseIterator):
    def __init__(self, book_shelf: BookShelf):
        self.book_shelf = book_shelf
        self.index: int = self.book_shelf.get_length() - 1

    def has_previous(self) -> bool:
        if self.index > -1:
            return True
        else:
            return False

    def previous(self) -> object:
        """ Get current book and move to previous
        """
        book: Book = self.book_shelf.get_book_at(self.index)
        self.index -= 1
        return book


def main():
    book_shelf = BookShelf()
    book_shelf.append_book(Book("Alice in wonder land"))
    book_shelf.append_book(Book("Yotsubato!"))
    book_shelf.append_book(Book("Chinderella"))
    book_shelf.append_book(Book("Harry Potter"))
    it: Iterator = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book.get_name())

    rit: ReverseIterator = book_shelf.reverse_iterator()
    while rit.has_previous():
        book = rit.previous()
        print(book.get_name())


if __name__ == "__main__":
    main()
