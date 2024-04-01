# collect of money (DRF)

Тестовый пет-проект на DRF по сбору денег
для разного рода нужд (ДР, свадьбы и тд.)


## Содержание

- [Содержание](#описание)
- [Технологии](#технологии)
- [Установка](#установка)
- [Инструкция](#инструкция)

## Технологии:

* [Python 3.10](https://www.python.org/)
* [Django 5.0.3](https://www.djangoproject.com/)
* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
* [Redis 5.0.3](https://developer.redis.com/)
* [Celery 5.3.6](https://docs.celeryq.dev/)
* [Gunicorn 21.2.0](https://gunicorn.org/)

## Установка

* Клонируйте гит репозиторий выполнив команду https://github.com/Nekketsu4/game_store.git 
* Перейдите в папку с клоном проекта "cd path/collect_of_money"
* Создайте виртуальное окружение выполнив команду "python3 -m venv venv"
* Активируйте виртуальное окружение выполнив команду "source venv/bin/activate"

```
git clone https://github.com/rg3915/django-experience.git
cd collect_of_money
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Инструкция

* Перед запуском приложения, создайте файл env.prod, затем зайдите в файл .env.example, скопируйте его содержимое в .env.prod и заполните поля
* Выполните команду "docker-compose -f docker-compose.prod.yaml up -d --build" - для сборки проекта
* Выполните миграцию "docker-compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput"
* Создайте суперпользователя(админа) 'docker-compose -f docker-compose.prod.yaml exec web python manage.py createsuperuser --username="admin" --email=""'

```
docker-compose -f docker-compose.prod.yaml up -d --build
docker-compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yaml exec web python manage.py createsuperuser --username="admin" --email=""
```