# TODO: описать базовый класс
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
            model: Модель устройства.
            manufacturer: Производитель устройства.
        """
        self._model = model
        self._manufacturer = manufacturer

    @property
    def model(self) -> str:
        """
         Свойство для получения модели устройства.

         Возвращает защищенный атрибут _model.
         """
        return self._model

    @property
    def manufacturer(self) -> str:
      """
         Свойство для получения производителя устройства.

         Возвращает защищенный атрибут _manufacturer.
         """
      return self._manufacturer

    def __str__(self) -> str:
      """
      Строковое представление объекта Device.
      Возвращает отформатированную строку с моделью и производителем.
      """
      return f"Устройство: {self.model}, Производитель: {self.manufacturer}"

    def __repr__(self) -> str:
      """
      Официальное строковое представление объекта Device.
       Позволяет однозначно воссоздать объект из строки.
       Использует f-строку и форматирование !r для представления атрибутов.
      """
      return f"{self.__class__.__name__}(model={self.model!r}, manufacturer={self.manufacturer!r})"

    def turn_on(self) -> str:
        """
        Метод включения устройства.

        Возвращает сообщение о включении устройства.
        """
        return "Устройство включено."

    def turn_off(self) -> str:
      """
        Метод выключения устройства.

        Возвращает сообщение о выключении устройства.
        """
      return "Устройство выключено."



# TODO: описать дочерний класс
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
          model: Модель смартфона.
          manufacturer: Производитель смартфона.
      os: Операционная система смартфона.
                battery_capacity: Ёмкость аккумулятора в мАч.
            """
      super().__init__(model, manufacturer)
      self._os = os  # Защищённый атрибут, доступ к нему через свойство.
      self._battery_capacity = battery_capacity  # Защищённый атрибут, доступ к нему через свойство.

    @property
    def os(self) -> str:
        """
          Свойство для получения операционной системы смартфона.

          Возвращает защищенный атрибут _os.
          """
        return self._os

    @property
    def battery_capacity(self) -> int:
        """
          Свойство для получения ёмкости аккумулятора смартфона.

          Возвращает защищенный атрибут _battery_capacity.
          """
        return self._battery_capacity

    def __str__(self) -> str:
        """
           Строковое представление объекта SmartPhone.
           Перегружает метод __str__ базового класса, добавляя информацию об ОС и ёмкости аккумулятора.
        """
        return f"Смартфон: {self.model}, Производитель: {self.manufacturer}, ОС: {self.os}, Батарея: {self.battery_capacity} мАч"

    def __repr__(self) -> str:
        """
          Официальное строковое представление объекта SmartPhone.
          Перегружает метод __repr__ базового класса, для включения информации об ОС и ёмкости аккумулятора.
       """
        return f"{self.__class__.__name__}(model={self.model!r}, manufacturer={self.manufacturer!r}, os={self.os!r}, battery_capacity={self.battery_capacity!r})"

    def turn_on(self) -> str:
        """
        Перегрузка метода включения из базового класса.

        Возвращает сообщение о включении смартфона с указанием модели.

        Переопределение происходит для конкретизации информации, когда включен конкретно смартфон.
        """
        return f"Смартфон {self.model} включен."

    def make_call(self, phone_number: str) -> str:
        """
        Метод для осуществления звонка.

        Args:
            phone_number: Номер телефона для звонка.
        Returns:
            Сообщение о совершении звонка на указанный номер.
        """
        return f"Звоню на номер {phone_number}."