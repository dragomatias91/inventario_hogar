# 🏠 Inventario del Hogar

Aplicación web desarrollada con Django para administrar el inventario del hogar. Permite gestionar productos, categorías y una lista de compras inteligente.

## 🛠️ Tecnologías
- Python
- Django
- Bootstrap 5
- SQLite

## 📦 Instalación

1. Clonar el repositorio
2. Crear y activar el entorno virtual
3. Instalar dependencias: `pip install -r requirements.txt`
4. Aplicar migraciones: `python manage.py migrate`
5. Crear superusuario: `python manage.py createsuperuser`
6. Levantar el servidor: `python manage.py runserver`

## 🚀 Orden de prueba

1. Entrar al admin en `/admin` y crear categorías
2. Crear productos asignándoles una categoría
3. Ver el listado de categorías en `/categorias`
4. Ver el listado de productos en `/productos`
5. Usar el buscador para filtrar productos por nombre
6. Ver la lista de compras en `/productos/compras`
7. Los productos con stock 0 aparecen automáticamente en la lista de compras
8. Al marcar un producto como comprado se actualiza el stock

## 📁 Estructura

- `core` → home y template base
- `categorias` → modelo y CRUD de categorías
- `productos` → modelo y CRUD de productos y lista de compras

## ✍️ Autor
Matias Drago