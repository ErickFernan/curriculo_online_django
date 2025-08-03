FROM python:3.10.0-alpine

LABEL maintainer="Erick <dverickfernan@gmail.com>"

# Instalar dependências do sistema
RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    build-base

# Criar diretório de trabalho
WORKDIR /var/www

# Copiar código para dentro da imagem
COPY . /var/www

# Instalar as dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Coletar arquivos estáticos (caso use)
RUN python manage.py collectstatic --noinput || true

# Porta padrão do Django
EXPOSE 8000

# Define o comando padrão (que será sobrescrito pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
