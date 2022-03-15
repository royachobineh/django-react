
FROM python:3.8.9

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install backports.zoneinfo

WORKDIR /app/django-api

# RUN python -m pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "localhost:8000"]