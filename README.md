## Структура проекта:
    /bot: код Telegram бота.
    /web: код FastAPI приложения.
    docker-compose.yml: файл конфигурации Docker Compose.
    Dockerfile: файлы Docker для сборки образов.
    nginx.conf: конфигурация Nginx.

## Описание
    Это приложение для создания и получения сообщений, 
    использующее FastAPI для веб-сервиса и aiogram для 
    Telegram бота. В проекте используются Docker и Docker 
    Compose для развертывания приложения, Redis для 
    кэширования и MongoDB для хранения данных.

## Настройка бота
    В /bot/bot.py замените API_TOKEN на ваш API TOKEN

## Настройка Docker и Docker Compose 
    Сборка Docker образов
    docker-compose build
    
    Запуск контейнеров
    docker-compose up

    Для отключения 
    docker-compose down

    Логирование 
    docker logs <имя_контейнера>

## Проверка статуса
    docker-compose ps   
    Вы должны увидеть контейнеры web, nginx, mongo, redis и bot в списке.
    
## Доступ к приложениям
    API сервер доступен на порту 8000:

    Получить сообщения GET: http://localhost:8000/api/v1/messages/
    Создать сообщение POST: http://localhost:8000/api/v1/message/