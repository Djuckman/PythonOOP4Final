from typing import Tuple


class Transport:
    """ Базовый класс Транспорта. """

    def __init__(self, model: str, price: int):
        '''
        self.model - модель транспорта
        self.price - цена транспорта
        '''
        if not isinstance(model, str) or not isinstance(price, int):
            raise TypeError
        self.model = model
        self.price = price

    def __str__(self):
        return f"Модель транспорта {self.model}; Стоимость транспорта {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, price={self.price!r})"

    def move(self, from_coord: Tuple[int, int], to_coord: Tuple[int, int]) -> bool:
        '''
        Передвижение транспорта из одной точки в другую
        from_coord - точка начала движения
        to_coord - точка конца движения
        Возвращает True, если транспорт доехал до точки назначения

        Перегружается, поскольку тип передвижения зависит от конкретного транспорта
        '''
        print(f"Транспорт передвигается из {from_coord} в {to_coord}")
        return True  # Заглушка

    def signal(self):
        '''
        Транспорт сигналит.
        Метод не перегружается, все типы транспорта гудят по одному принципу (допустим)
        '''
        print("Биииип!")


class Car(Transport):
    ''' Класс машина. '''

    def __init__(self, model: str, price: int):
        super().__init__(model, price)

    def __str__(self):
        return f"Модель машины {self.model}; Стоимость машины {self.price}"

    def move(self, from_coord: Tuple[int, int], to_coord: Tuple[int, int]) -> bool:
        print(f"Машина едет из {from_coord} в {to_coord}")
        return True  # Заглушка


class Ship(Transport):
    ''' Класс корабль. '''

    def __init__(self, model: str, price: int):
        super().__init__(model, price)

    def __str__(self):
        return f"Модель корабля {self.model}; Стоимость корабля {self.price}"

    def move(self, from_coord: Tuple[int, int], to_coord: Tuple[int, int]) -> bool:
        print(f"Корабль плывет из {from_coord} в {to_coord}")
        return True  # Заглушка


if __name__ == "__main__":
    # Write your solution here
    pass
