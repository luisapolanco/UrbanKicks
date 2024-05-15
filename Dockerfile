# Usamos la imagen oficial de Python para Django
FROM python:3.9-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos de requerimientos al directorio de trabajo
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install -r requirements.txt
RUN pip install requests

# Copiamos el resto de los archivos al directorio de trabajo
COPY . .

# Exponemos el puerto 8000, que es el puerto predeterminado de Django
EXPOSE 8000

# Ejecutamos el comando para iniciar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
