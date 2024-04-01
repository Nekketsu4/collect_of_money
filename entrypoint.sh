#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  #проверяем запущено ли БД или нет
  echo "database not yet run"

  #проверяем доступ к хосту и порту
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.5
  done

  echo "DB is running"

fi
# удаление устарвших данных
python manage.py flush --no-input
#выполнение миграции
python manage.py migrate

exec "$@"