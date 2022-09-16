FROM python:3-slim
LABEL maintainer="thiagojb12@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["gunicorn","app.wsgi:application","--bind","0.0.0.0:8000"] 