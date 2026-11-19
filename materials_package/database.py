import sqlite3

def init_db():
    """Создает файл базы данных и таблицу, если их еще нет."""
    with sqlite3.connect('calculations.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                material TEXT NOT NULL,
                area REAL NOT NULL,
                price REAL NOT NULL,
                quantity REAL NOT NULL,
                total_cost REAL NOT NULL
            )
        ''')
        conn.commit()


def save_calculation(material: str, area: float, price: float, quantity: float, total_cost: float):
    """Сохраняет результат одного расчета в базу данных."""
    # Открываем соединение
    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()

    # Выполняем запись
    cursor.execute('''
        INSERT INTO history (material, area, price, quantity, total_cost)
        VALUES (?, ?, ?, ?, ?)
    ''', (material, area, price, quantity, total_cost))

    # Фиксируем изменения и ОБЯЗАТЕЛЬНО закрываем файл
    conn.commit()
    conn.close()

    # Этот print появится в терминале (внизу), если запись прошла успешно
    print(f"DEBUG: Успешно сохранено в БД! {material}, {area}, {price}")