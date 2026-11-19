import pytest
from materials_package.models import WallPaper, Tile, Laminate


def test_wallpaper_calculation():
    # Вводим 50 кв.м. по цене 1000 руб.
    # Формула: (50 * 1.1) / 5 = 11 рулонов.
    obj = WallPaper(area=50, price=1000)

    # Проверяем, что количество = 11
    assert obj.calculate_quantity() == 11.0
    # Проверяем, что итоговая стоимость = 11000
    assert obj.get_price() == 11000


def test_tile_calculation():
    # Вводим 10 кв.м. по цене 500 руб.
    # Формула: 10 * 1.05 = 10.5 кв.м.
    obj = Tile(area=10, price=500)

    assert obj.calculate_quantity() == 10.5
    assert obj.get_price() == 5250


def test_negative_area_error():
    # Мы ожидаем, что при вводе отрицательной площади программа выдаст ошибку ValueError
    with pytest.raises(ValueError):
        WallPaper(area=-10, price=100)


def test_negative_price_error():
    # Проверяем, что цена не может быть отрицательной
    with pytest.raises(ValueError):
        Laminate(area=10, price=-50)