import pytest
from typing import List, Dict

class BooksCollector:

    def __init__(self):
        self.books_genre: Dict[str, str] = {}  # Книга: Жанр
        self.favorites: List[str] = []  # Избранные
        self.genre: List[str] = ['Фантастика', 'Ужасы', 'Драма', 'Комедия', 'Мультфильмы', 'Приключения', 'Детективы',
                                 'Фэнтези', 'Научная фантастика']  # Жанры (по ТЗ)
        self.genre_age_rating: List[str] = ['Ужасы', 'Детективы']  # Возрастные (по ТЗ)

    def add_new_book(self, name: str) -> None:
        if name not in self.books_genre:
            self.books_genre[name] = ''

    def set_book_genre(self, name: str, genre: str) -> None:
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name: str) -> str | None:
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre: str) -> List[str]:
        result = []
        for book, book_genre in self.books_genre.items():
            if book_genre == genre:
                result.append(book)
        return result

    def get_books_genre(self) -> Dict[str, str]:
        return self.books_genre

    def get_books_for_children(self) -> List[str]:
        result = []
        for book, genre in self.books_genre.items():
            if genre not in self.genre_age_rating:
                result.append(book)
        return result

    def add_book_in_favorites(self, name: str) -> None:
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def delete_book_from_favorites(self, name: str) -> None:
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorites_books(self) -> List[str]:
        return self.favorites


class TestBooksCollector:  # Тесты тоже оставляем

    def test_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        assert 'Книга1' in collector.books_genre

    def test_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_book_genre('Книга1') == 'Фантастика'

    def test_get_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Драма')
        assert collector.get_book_genre('Книга1') == 'Драма'
        assert collector.get_book_genre('Книга2') is None

    @pytest.mark.parametrize("genre, expected_books", [
        ('Фантастика', ['Книга1', 'Книга3']),
        ('Детективы', ['Книга2']),
        ('НетТакого', [])
    ])
    def test_get_books_by_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.set_book_genre('Книга2', 'Детективы')
        collector.set_book_genre('Книга3', 'Фантастика')
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_all_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Комедия')
        assert collector.get_books_genre() == {'Книга1': 'Комедия'}

    def test_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Фэнтези')
        collector.set_book_genre('Книга2', 'Ужасы')
        assert collector.get_books_for_children() == ['Книга1']

    def test_add_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert 'Книга1' in collector.favorites

        collector.add_book_in_favorites('Книга2')  # Добавляем несуществующую
        assert 'Книга2' not in collector.favorites

    def test_delete_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        collector.delete_book_from_favorites('Книга1')
        assert 'Книга1' not in collector.favorites

    def test_get_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert collector.get_list_of_favorites_books() == ['Книга1']

    def test_add_existing_book(self):  # Проверка на дубликаты.
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_new_book("Книга")
        assert len(collector.get_books_genre()) == 1

    def test_set_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("НетКниги", "Фантастика")
        assert "НетКниги" not in collector.get_books_genre()

    def test_add_favorite_nonexistent(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("НетКниги")
        assert len(collector.favorites) == 0

    def test_delete_favorite_nonexistent(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("НетКниги")
        assert len(collector.favorites) == 0