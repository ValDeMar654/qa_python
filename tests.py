import pytest


class TestBooksCollector:

    def test_init_books_genre(self, collector):
        assert type(collector.books_genre) is dict
        assert len(collector.books_genre) == 0

    def test_init_favorites(self, collector):
        assert type(collector.favorites) is list
        assert len(collector.favorites) == 0

    def test_init_genre(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы',
                                   'Детективы', 'Мультфильмы', 'Комедии']

    def test_init_genre_age_rating(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book', ['', 'Z' * 50])
    def test_add_new_book_with_invalid_name(self, collector, book):
        collector.add_new_book(book)
        assert book not in collector.books_genre

    def test_set_book_genre_book_in_books_genre_genre_in_genre(self,
                                                               collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre[
            'Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_set_book_genre_book_in_books_genre_genre_not_in_genre(self,
                                                                   collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre(
            'Гордость и предубеждение и зомби', 'Комиксы')
        assert not collector.books_genre[
            'Гордость и предубеждение и зомби'] is None

    def test_get_book_genre_book_in_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre(
            'Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_one_book_in_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre(
            'Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        assert type(collector.get_books_with_specific_genre(
            'Мультфильмы')) is list
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 1

    def test_get_books_with_specific_genre_empty_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert type(collector.get_books_with_specific_genre(
            'Мультфильмы')) is list
        assert len(collector.get_books_with_specific_genre('Мультфильмы')) == 0

    def test_get_books_genre_two_books_in_dict(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre(
            'Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        assert type(collector.get_books_genre()) is dict
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_one_book_in_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre(
            'Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        assert type(collector.get_books_for_children()) is list
        assert len(collector.get_books_for_children()) == 1

    def test_get_books_for_children_empty_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre(
            'Что делать, если ваш кот хочет вас убить', 'Детективы')
        assert type(collector.get_books_for_children()) is list
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_add_one_one_in_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites(
            'Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_add_two_del_one_one_in_list(self,
                                                                    collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites(
            'Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites(
            'Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_one_added_one_in_list(self,
                                                               collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites(
            'Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_no_one_added_empty_list(self,
                                                                 collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert type(collector.get_list_of_favorites_books()) is list
        assert len(collector.get_list_of_favorites_books()) == 0
