#образ питона для проекта
FROM python:3.10-alpine

#переменные окружения для питона
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#рабочая папка проекта
WORKDIR /usr/src/app

#зависимости для postgres
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

#установка зависимостей проекта
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

#указываем путь куда скопируем наш проект в контейнере
COPY . /usr/src/app

#пробрасываем порт контейнера
EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]