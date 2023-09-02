### Структура директории `/app`

```
/app
|-- Dockerfile
|-- app.py
|-- api.yml
|-- test_app.py
|-- requirements.txt
```

### Инструкции по сборке и запуску

Чтобы собрать и запустить образ Docker:

```bash
# Переходим в директорию /app
cd /app

# Собираем образ Docker
docker build -t app .

# Запускаем контейнер, передавая необходимые переменные окружения
docker run -d -p 8000:8000 -e AUTHOR=cloudru -e UUID=your_uuid app
```

Теперь приложение доступно на порту 8000.

export AUTHOR=<your-uuid-value>
export UUID=<your-uuid-value>
curl http://127.0.0.1:8000/id
