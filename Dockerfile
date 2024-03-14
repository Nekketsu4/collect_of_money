FROM python:3.10

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./req.txt ./
RUN pip install -r req.txt

COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]