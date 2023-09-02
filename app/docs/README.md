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

### Теперь приложение доступно на порту 8000.

# Инструкция по работе с Docker
## Установка переменных окружения
```bash
export AUTHOR=<your-uuid-value>
export UUID=<your-uuid-value>
curl http://127.0.0.1:8000/id
```
## Проверка аккаунта Docker
```bash
docker login
cat ~/.docker/config.json | grep "auths"
```
## Тегирование и загрузка образа в Docker Hub
```bash
docker commit <SHAconteiner> pavbuy/cloudru:latest
docker push pavbuy/cloudru:latest
docker pull pavbuy/cloudru:latest
```
## Ссылка на Docker Hub
[Посмотреть теги образа на Docker Hub](https://hub.docker.com/r/pavbuy/cloudru/tags)