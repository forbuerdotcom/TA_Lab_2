import os
import sqlite3

import pytest
from docx import Document

from materials_package.models import Entity, WallPaper, Tile, Laminate
from materials_package.reporter import save_report_to_word
from materials_package.database import init_db, save_calculation


# ---------- Расчёты ----------

def test_wallpaper_calculation():
    # 50 кв.м по 1000 руб.: (50 * 1.1) / 5 = 11 рулонов
    obj = WallPaper(area=50, price=1000)
    assert obj.calculate_quantity() == 11.0
    assert obj.get_price() == 11000


def test_wallpaper_ceil_rounding():
    # 10 кв.м: (10 * 1.1) / 5 = 2.2 -> округляем вверх до 3 целых рулонов
    obj = WallPaper(area=10, price=100)
    assert obj.calculate_quantity() == 3.0
    assert obj.get_price() == 300


def test_tile_calculation():
    # 10 кв.м по 500 руб.: 10 * 1.05 = 10.5 кв.м
    obj = Tile(area=10, price=500)
    assert obj.calculate_quantity() == 10.5
    assert obj.get_price() == 5250


def test_laminate_calculation():
    # 20 кв.м по 800 руб.: 20 * 1.05 = 21 кв.м
    obj = Laminate(area=20, price=800)
    assert obj.calculate_quantity() == 21.0
    assert obj.get_price() == 16800


def test_get_unit():
    assert WallPaper(area=1, price=1).get_unit() == "рулонов"
    assert Tile(area=1, price=1).get_unit() == "кв.м"
    assert Laminate(area=1, price=1).get_unit() == "кв.м"


# ---------- Валидация (managed-атрибуты) ----------

def test_negative_area_error():
    with pytest.raises(ValueError):
        WallPaper(area=-10, price=100)


def test_zero_area_error():
    # Площадь должна быть строго больше 0
    with pytest.raises(ValueError):
        Tile(area=0, price=100)


def test_negative_price_error():
    with pytest.raises(ValueError):
        Laminate(area=10, price=-50)


def test_zero_price_allowed():
    # Нулевая цена допустима — проверяем, что не выбрасывается исключение
    obj = Laminate(area=10, price=0)
    assert obj.get_price() == 0


# ---------- DUNDER-методы ----------

def test_str_contains_class_name_and_data():
    obj = WallPaper(area=50, price=1000)
    s = str(obj)
    assert "Обои" in s
    assert "50" in s
    assert "1000" in s


def test_repr_contains_class_name_and_params():
    obj = Tile(area=10, price=500)
    r = repr(obj)
    assert "Tile" in r
    assert "area=10" in r
    assert "price=500" in r


def test_inheritance_and_abstract():
    # Все материалы наследуются от Entity, Entity нельзя инстанцировать напрямую
    assert issubclass(WallPaper, Entity)
    assert issubclass(Tile, Entity)
    assert issubclass(Laminate, Entity)
    with pytest.raises(TypeError):
        Entity(area=10, price=100)


# ---------- База данных ----------

def test_database_save_and_read():
    init_db()
    save_calculation("Обои", 50, 1000, 11, 11000)

    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT material, area, price, quantity, total_cost FROM history "
        "WHERE material = ? AND area = ?",
        ("Обои", 50),
    )
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    assert row[0] == "Обои"
    assert row[1] == 50
    assert row[4] == 11000


# ---------- Отчёт Word ----------

def test_save_report_to_word(tmp_path):
    # tmp_path — временная папка, которую pytest создаёт и удаляет сам
    filepath = tmp_path / "test_report.docx"
    text = "Материал: Обои\nПлощадь: 50 кв.м.\nИТОГО: 11000 руб."
    save_report_to_word(str(filepath), text)

    assert filepath.exists()

    doc = Document(str(filepath))
    paragraphs = [p.text for p in doc.paragraphs]
    assert "Материал: Обои" in paragraphs
    assert "ИТОГО: 11000 руб." in paragraphs