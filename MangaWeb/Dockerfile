# Utiliza una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /code

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /code/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio del proyecto al directorio de trabajo
COPY . /code/

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=MangaWeb.settings

#RUN pip install gunicorn

#CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 MangaWeb.wsgi:application
