FROM python:3.10.0-alpine

LABEL maintainer="Erick <dverickfernan@gmail.com>"

RUN mkdir -p /usr/src/app
# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
ADD . /usr/src/app

# Coletar arquivos estáticos (caso use)
RUN python manage.py collectstatic --noinput || true

# Porta padrão do Django
EXPOSE 8000
