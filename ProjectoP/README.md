
Este es un proyecto de una tienda online desarrollado con Django. Permite a los usuarios agregar productos, categorías y clientes, así como realizar búsquedas en la base de datos.

## Instalación

1. Clona este repositorio en tu máquina local utilizando `git clone`.

2. Crea un entorno virtual para el proyecto:
python -m venv venv
3. Activa el entorno virtual:
En Windows: venv\Scripts\activate
En macOS y Linux: source venv/bin/activate
4. Instala las dependencias del proyecto:
pip install -r requirements.txt
5. Aplica las migraciones:
python manage.py migrate
6. Crea un superusuario:
python manage.py createsuperuser
7. Inicia el servidor de desarrollo:
python manage.py runserver
8. Abre tu navegador y visita http://127.0.0.1:8000 para acceder a la aplicación.

## Funcionalidades
Agregar Producto: Permite agregar productos a la base de datos con información como nombre, precio y descripción.
Agregar Categoría: Permite agregar categorías con nombre y descripción.
Agregar Cliente: Permite agregar clientes con nombre y correo electrónico.
Buscar: Realiza búsquedas en la base de datos de productos según el término ingresado.
Administrador: Accede a la interfaz de administración de Django para gestionar los datos.

## Tecnologías Utilizadas
Django: Framework de desarrollo web en Python.
HTML/CSS: Para la estructura y el estilo de las páginas.

## Autor
Maria Paz Muller
mpazmuller@gmail.com

