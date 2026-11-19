
FROM python:3.10-slim

# Устанавливаем системные библиотеки для работы с графикой (tkinter)
RUN apt-get update && apt-get install -y python3-tk && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы проекта внутрь контейнера
COPY . .

# По умолчанию при запуске контейнера будут запускаться тесты.
CMD ["pytest", "-v"]