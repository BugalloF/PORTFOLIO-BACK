# Usamos una imagen oficial de Python
FROM python:3.12

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos del proyecto al contenedor
COPY . .

# Instalamos las dependencias de sistema necesarias para Pillow
RUN apt-get update && apt-get install -y zlib1g-dev libjpeg-dev

# Instalamos las dependencias del proyecto sin usar caché
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto en el que corre Django (normalmente 8000)
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:${PORT} portfolio_back.wsgi:application
