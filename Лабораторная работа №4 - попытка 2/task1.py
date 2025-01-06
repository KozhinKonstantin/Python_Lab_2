
class Device:
    """
    Базовый класс для электронных устройств.

    Определяет общие свойства и поведение для всех устройств.
    """

    def __init__(self, model: str, manufacturer: str):
        """
        Конструктор для класса Device.

        Инициализирует устройство с моделью и производителем.
        _model - защищенный атрибут, доступ к нему через свойство.
        _manufacturer - защищенный атрибут, доступ к нему через свойство.

        Args:
            model: Модель устройства (строка).
            manufacturer: Производитель устройства (строка).
        """
        # Атрибуты _model и _manufacturer являются "защищенными" (непубличными) - доступ к ним
        # осуществляется через свойства model и manufacturer. Это делается для инкапсуляции данных
        # и контроля доступа к атрибутам. Прямое обращение к этим атрибутам извне не рекомендуется.
        self._model = model
        self._manufacturer = manufacturer

    @property
    def model(self) -> str:
        """
        Свойство для получения модели устройства.

        Возвращает защищенный атрибут _model.

        Returns:
            Модель устройства (строка).
        """
        # Свойство model предоставляет контролируемый способ доступа к _model.
        # Это позволяет, например, добавить логику для валидации данных при изменении
        # модели в будущем, если это понадобится.
        return self._model

    @property
    def manufacturer(self) -> str:
        """
        Свойство для получения производителя устройства.

        Возвращает защищенный атрибут _manufacturer.

        Returns:
           Производитель устройства (строка).
        """
        # Аналогично свойству model, это свойство обеспечивает контролируемый доступ
        # к атрибуту _manufacturer, защищая данные от случайных или некорректных изменений.
        return self._manufacturer

    def __str__(self) -> str:
        """
        Строковое представление объекта Device.

        Возвращает отформатированную строку с моделью и производителем.

        Returns:
            Строковое представление устройства (строка).
        """
        return f"Устройство: {self.model}, Производитель: {self.manufacturer}"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта Device.

        Позволяет однозначно воссоздать объект из строки.
        Использует f-строку и форматирование !r для представления атрибутов.

        Returns:
             Официальное строковое представление объекта (строка).
        """
        return f"{self.__class__.__name__}(model={self.model!r}, manufacturer={self.manufacturer!r})"

    def turn_on(self) -> str:
        """
        Включает устройство.

        Возвращает сообщение о включении устройства.

        Returns:
            Сообщение о включении устройства (строка).
        """
        return "Устройство включено."

    def turn_off(self) -> str:
        """
        Выключает устройство.

        Возвращает сообщение о выключении устройства.

        Returns:
            Сообщение о выключении устройства (строка).
        """
        return "Устройство выключено."


class SmartPhone(Device):
    """
    Класс смартфона, наследник класса Device.

    Описывает характеристики и поведение смартфона.
    """

    def __init__(self, model: str, manufacturer: str, os: str, battery_capacity: int):
        """
        Конструктор класса SmartPhone.

        Расширяет конструктор базового класса Device, добавляя операционную систему и ёмкость аккумулятора.

        Args:
          model: Модель смартфона (строка).
          manufacturer: Производитель смартфона (строка).
          os: Операционная система смартфона (строка).
          battery_capacity: Ёмкость аккумулятора в мАч (целое число).
        """
        # Вызов конструктора базового класса (Device) для инициализации модели и производителя.
        # Наследование позволяет повторно использовать код из базового класса, что уменьшает
        # дублирование кода и упрощает сопровождение.
        super().__init__(model, manufacturer)
        # Атрибуты _os и _battery_capacity являются защищенными, доступ к ним через свойства os и battery_capacity.
        self._os = os
        self._battery_capacity = battery_capacity

    @property
    def os(self) -> str:
        """
          Свойство для получения операционной системы смартфона.

          Возвращает защищенный атрибут _os.

          Returns:
              Операционная система смартфона (строка).
          """
        # Свойство os предоставляет контролируемый способ доступа к атрибуту _os.
        return self._os

    @property
    def battery_capacity(self) -> int:
        """
          Свойство для получения ёмкости аккумулятора смартфона.

          Возвращает защищенный атрибут _battery_capacity.

          Returns:
              Ёмкость аккумулятора смартфона (целое число).
          """
        # Свойство battery_capacity предоставляет контролируемый способ доступа к атрибуту _battery_capacity.
        return self._battery_capacity

    def __str__(self) -> str:
        """
        Строковое представление объекта SmartPhone.

        Перегружает метод __str__ базового класса, добавляя информацию об ОС и ёмкости аккумулятора.

        Returns:
           Строковое представление смартфона (строка).
        """
        # Перегрузка метода __str__ позволяет изменить строковое представление объекта SmartPhone,
        # добавив к нему специфичную информацию (ОС и емкость батареи).
        return f"Смартфон: {self.model}, Производитель: {self.manufacturer}, ОС: {self.os}, Батарея: {self.battery_capacity} мАч"

    def __repr__(self) -> str:
        """
        Официальное строковое представление объекта SmartPhone.

        Перегружает метод __repr__ базового класса, для включения информации об ОС и ёмкости аккумулятора.

        Returns:
            Официальное строковое представление смартфона (строка).
        """
        # Перегрузка метода __repr__ позволяет изменить официальное строковое представление
        # объекта SmartPhone, чтобы оно включало специфичные для смартфона атрибуты.
        return f"{self.__class__.__name__}(model={self.model!r}, manufacturer={self.manufacturer!r}, os={self.os!r}, battery_capacity={self.battery_capacity!r})"




