# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Car:
    """Представляет автомобиль с моделью, годом выпуска и пробегом."""

    def __init__(self, model: str, year: int, mileage: int) -> None:
        """Инициализирует объект Car.
        Args:
            model: Модель автомобиля (например, "Toyota Camry"). Не должна быть пустой.
            year: Год выпуска автомобиля. Должен быть положительным целым числом.
            mileage: Текущий пробег автомобиля. Должен быть неотрицательным.
        Raises:
            ValueError: Если модель пустая, год не положительный, или пробег отрицательный.
        """
        if not isinstance(model,str):
            raise TypeError
        if not isinstance(year,int):
            raise TypeError
        if not isinstance(mileage,int):
            raise TypeError
        if not model:
            raise ValueError("Модель не может быть пустой.")
        if year <= 0:
            raise ValueError("Год должен быть положительным целым числом.")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным.")
        self.model: str = model
        self.year: int = year
        self.mileage: int = mileage

    def drive(self, distance: int) -> None:
        """Симулирует поездку автомобиля на указанное расстояние.
        Args:
            distance: Расстояние поездки в километрах. Должно быть неотрицательным.
        Raises:
            ValueError: Если расстояние отрицательное.
        """
        if not isinstance(distance, int):
            raise TypeError
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")
        self.mileage += distance

    def get_age(self) -> int:
        """Вычисляет возраст автомобиля в годах (приблизительно).
        Returns:
            Возраст автомобиля в годах.  Может быть неточным, если вызывается не в текущем году.
        >>> car = Car("Honda Civic", 2020, 50000)
        >>> car.get_age()
        4
        """

        current_year = 2024
        return current_year - self.year
# TODO: описать ещё класс
class Dog:
    """Представляет собаку с именем, породой и возрастом."""

    def __init__(self, name: str, breed: str, age: int = 0) -> None:
        """Инициализирует объект Dog.
        Args:
            name: Имя собаки. Не должно быть пустым.
            breed: Порода собаки. Не должна быть пустой.
            age: Возраст собаки в годах. Должен быть неотрицательным. По умолчанию 0.
        Raises:
            ValueError: Если имя или порода пустые, или возраст отрицательный.
        """
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(breed, str):
            raise TypeError
        if not isinstance(age, int):
            raise TypeError

        if not name:
            raise ValueError("Имя не может быть пустым.")
        if not breed:
            raise ValueError("Порода не может быть пустой.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name: str = name
        self.breed: str = breed
        self.age: int = age

    def bark(self, times: int = 1) -> None:
        """Заставляет собаку лаять указанное количество раз.
        Args:
            times: Количество раз, которое собака должна лаять. Должно быть положительным. По умолчанию 1.
        Raises:
            ValueError: если times не положительное.
        """
        if not isinstance(times, int):
            raise TypeError
        if times <= 0:
            raise ValueError("Количество раз должно быть положительным целым числом.")
        print("Гав!" * times)

    def get_info(self) -> str:
        """Возвращает информацию о собаке.
        Returns:
            Строка, содержащая имя, породу и возраст собаки.
        >>> dog = Dog("Дружок", "Золотистый ретривер", 3)
        >>> dog.get_info()
        'Имя: Дружок, Порода: Золотистый ретривер, Возраст: 3'
        """
        return f"Имя: {self.name}, Порода: {self.breed}, Возраст: {self.age}"

# TODO: и ещё один
class BankAccount:
    """Представляет банковский счёт с балансом и владельцем."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        """Инициализирует объект BankAccount.
        Args:
            owner: Имя владельца счёта. Не должно быть пустым.
            initial_balance: Начальный баланс счёта. Должен быть неотрицательным. По умолчанию 0.0.
        Raises:
            ValueError: Если имя владельца пустое или начальный баланс отрицательный.
        """
        if not isinstance(owner, str):
            raise TypeError
        if not isinstance(initial_balance, float):
            raise TypeError

        if not owner:
            raise ValueError("Имя владельца не может быть пустым.")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner: str = owner
        self.balance: float = initial_balance

    def deposit(self, amount: float) -> float:
        """Вносит деньги на счёт.
        Args:
            amount: Сумма для внесения. Должна быть положительной.
        Returns:
            Новый баланс счёта.
        Raises:
            ValueError: Если сумма не положительная.
        >>> account = BankAccount("Алиса", 100.0)
        >>> account.deposit(50.0)
        150.0
        """
        if not isinstance(amount, float):
            raise TypeError
        if amount <= 0:
            raise ValueError("Сумма вклада должна быть положительной.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Снимает деньги со счёта.
        Args:
            amount: Сумма для снятия. Должна быть положительной и не превышать баланс.
        Returns:
            Новый баланс счёта.
        Raises:
            ValueError: Если сумма не положительная или превышает баланс.
        >>> account = BankAccount("Боб", 200.0)
        >>> account.withdraw(100.0)
        100.0
        """
        if not isinstance(amount, float):
            raise TypeError
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Сумма снятия превышает баланс.")
        self.balance -= amount
        return self.balance

