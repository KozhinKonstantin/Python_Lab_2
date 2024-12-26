class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        """
        Конструктор класса Book.

        Инициализирует объект книги с заданным именем и автором.
        _name и _author - защищенные атрибуты, доступ к которым рекомендуется через свойства.
        """
        self._name = name  # Используем _name для обозначения защищенного атрибута
        self._author = author

    @property
    def name(self):
        """
        Свойство для получения имени книги.

        Возвращает защищенный атрибут _name.
        """
        return self._name

    @property
    def author(self):
        """
        Свойство для получения автора книги.

        Возвращает защищенный атрибут _author.
        """
        return self._author

    def __str__(self):
        """
        Строковое представление объекта Book.

        Возвращает форматированную строку, представляющую книгу.
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
      """
        Строковое представление объекта Book.

        Позволяет однозначно воссоздать объект из строки.
        """
      return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Конструктор класса PaperBook.

        Инициализирует объект бумажной книги, вызывая конструктор базового класса (Book)
        и добавляя количество страниц.
        """
        super().__init__(name, author) # Вызов конструктора базового класса
        self._pages = pages

    @property
    def pages(self):
        """
        Свойство для получения количества страниц в бумажной книге.

        Возвращает защищенный атрибут _pages.
        """
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        """
        Сеттер для установки количества страниц.

        Устанавливает значение атрибута _pages после проверки типа и значения.
        Вызывает TypeError, если pages не является целым числом.
        Вызывает ValueError, если pages меньше или равно нулю.
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = pages

        def __str__(self):
            """
            Строковое представление объекта PaperBook.

            Переопределяет метод __str__ из базового класса для добавления информации о количестве страниц.
            """
            return f"Бумажная книга {self.name}. Автор {self.author}, {self.pages} страниц."
class AudioBook(Book):
        """Класс аудиокниги."""

        def __init__(self, name: str, author: str, duration: float):
            """
             Конструктор класса AudioBook.
             Инициализирует объект аудиокниги, вызывая конструктор базового класса и добавляя длительность.
            """
            super().__init__(name, author)  # Вызов конструктора базового класса
            self._duration = duration

        @property
        def duration(self):
            """
            Свойство для получения продолжительности аудиокниги.

            Возвращает защищенный атрибут _duration.
            """
            return self._duration

        @duration.setter
        def duration(self, duration: float):
            """
              Сеттер для установки продолжительности аудиокниги.
              Устанавливает значение атрибута _duration после проверки типа и значения.
              Вызывает TypeError, если duration не является числом.
              Вызывает ValueError, если duration меньше или равно нулю.
            """
            if not isinstance(duration, (int, float)):
                raise TypeError("Продолжительность должна быть числом.")
            if duration <= 0:
                raise ValueError("Продолжительность должна быть больше нуля.")
            self._duration = duration

        def __str__(self):
            """
              Строковое представление объекта AudioBook.

              Переопределяет метод __str__ из базового класса для добавления информации о длительности.
              """
            return f"Аудиокнига {self.name}. Автор {self.author}, продолжительность {self.duration:.2f} часов."