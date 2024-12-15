BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO: написать класс Book
class Book:
    """Представляет книгу с идентификатором, названием и количеством страниц.

        Атрибуты:
            id (int): Уникальный идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге (должно быть положительным числом).

        Методы:
            __init__(self, id_: int, name: str, pages: int): Конструктор класса. Инициализирует атрибуты книги.  Проверяет корректность типов данных и значения количества страниц.
            __str__(self) -> str: Возвращает строковое представление книги в формате "Книга "название_книги"".
            __repr__(self) -> str: Возвращает строковое представление, пригодное для воссоздания объекта с помощью функции eval().
        """

    def __init__(self, id_: int, name: str, pages: int):
        """Инициализирует объект Book.

        Args:
            id_: Уникальный идентификатор книги (целое число).
            name: Название книги (строка).
            pages: Количество страниц в книге (целое число, должно быть положительным).

        Raises:
            ValueError: если pages не является положительным целым числом.
            TypeError: если id_ или name имеют неверный тип.
        """
        if not isinstance(id_, int):
            raise TypeError("id_ должен быть целым числом.")
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages должен быть положительным целым числом.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """Возвращает строковое представление, пригодное для воссоздания объекта."""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"
# TODO: написать класс Library
class Library:

    """Представляет библиотеку, хранящую список книг.

    Атрибуты:
        books (List[Book]): Список объектов класса Book, хранящий информацию о книгах в библиотеке.

    Методы:
        __init__(self, books: List[Book] = None): Конструктор класса. Инициализирует библиотеку пустым списком книг, если books не предоставлен, иначе использует переданный список.
        get_next_book_id(self) -> int: Возвращает следующий доступный идентификатор для новой книги.  Если библиотека пуста, возвращает 1; иначе возвращает идентификатор последней книги + 1.
        get_index_by_book_id(self, book_id: int) -> int:  Возвращает индекс книги в списке по её идентификатору.  Если книга с указанным id не найдена, вызывает исключение ValueError.
    """

    def __init__(self, books=None):
        """Инициализирует объект Library.

        Args:
            books: Необязательный аргумент, список объектов Book. По умолчанию инициализируется пустым списком.
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """Возвращает следующий доступный ID для новой книги.

        Returns:
            Следующий доступный ID (целое число).
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        """Возвращает индекс книги в списке по её ID.

        Args:
            book_id: ID книги (целое число).

        Returns:
            Индекс книги в списке (целое число).

        Raises:
            ValueError: Если книга с указанным ID не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
