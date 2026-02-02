# qa_python
## Фикстуры
    - collector - экземпляр класса BooksCollector

## Группы тестов

### Тесты метода __init__
    - тест словаря books_genre
    - тест списка Избранных книг
    - тест списка Жанров
    - тест списка Жанров с возрастным ограничением

### Тесты добавления книг
    - тест метода add_new_book
    - тест метода add_new_book с невалидными именами (с применением параметризации)

### Тесты с жанрами
    - тест метода set_book_genre (жанр есть в списке)
    - тест метода set_book_genre (жанра нет в списке)

### Тесты с данными
    - тест метода get_book_genre
    - тест метода get_books_with_specific_genre (в жанре есть подходящие книги)
    - тест метода get_books_with_specific_genre (в жанре нет подходящих книг)
    - тест метода get_books_genre
    - тест метода get_books_for_children (в словаре есть подходящие книги)
    - тест метода get_books_for_children (в словаре нет подходящих книг)

### Тесты со списком Избранных книг
    - тест метода add_book_in_favorites
    - тест метода delete_book_from_favorites
    - тест метода get_list_of_favorites_books (с 1 добавленной книгой)
    - тест метода get_list_of_favorites_books (без добавленных книг)