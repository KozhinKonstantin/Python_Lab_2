from task_1 import Car,Dog,BankAccount # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    car = Car("Honda Civic", 2020, 50000)
    dog = Dog("Дружок", "Овчарка", 5)
    account = BankAccount("Евгений", 500)
    try:
     car.drive("сто")# TODO: вызвать метод с некорректными аргументами(b)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     dog.bark("два")# TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     account.deposit("минус сто")# TODO: вызвать метод с некорректными аргументами(a)
    except TypeError:
        print('Ошибка: неправильные данные')
