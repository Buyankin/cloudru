# Этап 1: Сборка
FROM python:3.9-slim AS build
# Устанавливаем рабочую директорию в контейнере
WORKDIR /app
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip install --no-cache-dir -r requirements.txt

# Этап 2: Запуск
FROM python:3.9-slim
WORKDIR /app
# Копирование Python зависимостей из первого этапа
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
# Копирование файлов вашего приложения
COPY . .
# Пользователь от имени которого будут выполняться последующие команды внутри образа Docker.
USER cloudru
# Задаем переменную окружения
ENV FLASK_APP=app:app
ENV AUTHOR=docker_buyankin_env
# Открываем порт 8000
EXPOSE 8000
# Команда для запуска приложения через gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
# Добавить метаданные к Docker-образу
LABEL maintainer="Pavel Buyankin"