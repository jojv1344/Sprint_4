import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2
    
    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        
        assert len(collector.books_genre) == 0

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение' + ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')  # 41 символ
        
        assert len(collector.books_genre) == 0

    def test_add_new_book_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        
        assert collector.get_book_genre('1984') == ''

    def test_set_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        collector.set_book_genre('451 градус по Фаренгейту', 'Фантастика')
        
        assert collector.get_book_genre('451 градус по Фаренгейту') == 'Фантастика'

    def test_set_book_genre_non_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Детективы')
        
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маяк на краю света')
        collector.set_book_genre('Маяк на краю света', 'Приключения')
        
        assert collector.get_book_genre('Маяк на краю света') == 'Приключения'

    def test_get_book_genre_non_existing_book(self):
        collector = BooksCollector()
        
        assert collector.get_book_genre('Несуществующая книга') is None

    @pytest.mark.parametrize("genre,expected_count", [
        ('Фантастика', 1),
        ('Ужасы', 0),
        ('Детективы', 0)
    ])
    def test_get_books_with_specific_genre(self, genre, expected_count):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        
        assert len(collector.get_books_with_specific_genre(genre)) == expected_count

    def test_age_rating_exclusion(self):
        collector = BooksCollector()
        collector.add_new_book('Печальные призраки')
        collector.set_book_genre('Печальные призраки', 'Ужасы')
        
        children_books = collector.get_books_with_specific_genre('Детские книги')
        assert 'Печальные призраки' not in children_books