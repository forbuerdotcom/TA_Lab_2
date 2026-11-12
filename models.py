from abc import ABC, abstractmethod
import math

class Entity(ABC):
    def __init__(self, area: float, price: float):
        self.area = area
        self.price = price

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value <= 0:
            raise ValueError("Плозадь должна быть больше 0!")
        self._area = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self._price = value



    @abstractmethod
    def calculate_quantity(self) ->float:
        pass

    @abstractmethod
    def get_unit(self) -> str:
        pass

    def get_price(self) -> float:
        return self.calculate_quantity() * self.price


class WallPaper(Entity):
    def calculate_quantity(self) -> float:
        area_with_waste = self.area * 1.1
        rolls = round(area_with_waste / 5, 2)
        return float(math.ceil(rolls))

    def get_unit(self) -> str:
        return "рулонов"

class Tile(Entity):
    def calculate_quantity(self) -> float:
        area_with_waste = self.area * 1.05
        return area_with_waste

    def get_unit(self) -> str:
        return "кв.м"

class Laminate(Entity):
    def calculate_quantity(self) -> float:
        area_with_waste = self.area * 1.05
        return area_with_waste

    def get_unit(self) -> str:
        return "кв.м"


