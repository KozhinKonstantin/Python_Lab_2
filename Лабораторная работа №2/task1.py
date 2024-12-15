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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
