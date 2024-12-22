class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name  # Используем _name для обозначения защищенного атрибута
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}, {self.pages} страниц."


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self._duration = duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}, продолжительность {self.duration:.2f} часов."
