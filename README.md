# 🏠 Inventario del Hogar

Aplicación web desarrollada con Django para administrar el inventario del hogar.

##  Tecnologías
- Python
- Django
- Bootstrap 5

##  Instalación

1. Clonar el repositorio
2. Crear y activar el entorno virtual
3. Instalar dependencias: `pip install -r requirements.txt`
4. Aplicar migraciones: `python manage.py migrate`
5. Crear superusuario: `python manage.py createsuperuser`
6. Levantar el servidor: `python manage.py runserver`

##  Orden de prueba

1. Registrarse en `/accounts/register` o iniciar sesión en `/accounts/login`
2. Ver categorías en `/categorias`
3. Ver productos en `/productos` — usar buscador y filtros
4. Ver lista de compras en `/productos/compras`
5. Ver about en `/about`
6. Acceder al admin en `/admin`

##  Paso a paso de construcción

### 1. Configuración inicial
- Creación del proyecto `inventario_hogar`
- Creación de las apps: `core`, `categorias`, `productos`, `accounts`
- Registro de las apps en `settings.py`
- Configuración de idioma español (`LANGUAGE_CODE = 'es-ar'`)

### 2. App Categorias
- Creación del modelo `Categoria` (nombre, descripcion)
- Migraciones y registro en admin
- Configuración del admin con `list_display` y `search_fields`
- Creación de `forms.py` con `CategoriaForm`
- CRUD completo: listar, crear, editar, eliminar
- Buscador por nombre
- Orden alfabético con `Lower`

### 3. App Productos
- Creación del modelo `Producto` con `TextChoices` para unidad de medida y ubicación
- Creación del modelo `ListaCompras` con FK a Producto
- Migraciones y registro en admin
- Configuración del admin con `list_display`, `search_fields` y `list_filter`
- Creación de `forms.py` con `ProductoForm` y `ListaComprasForm`
- CRUD completo para Producto y ListaCompras
- Buscador por nombre
- Filtros por ubicación, categoría y disponible
- Orden alfabético con `Lower`
- Lista de compras inteligente: muestra productos con stock 0
- Vista `marcar_comprado` que actualiza el stock al confirmar cantidad comprada

### 4. App Core
- Creación de `base.html` con navbar y Bootstrap 5
- Vista y template `home` con hero section
- Vista y template `about`
- Conexión de URLs de todas las apps en `config/urls.py`

### 5. App Accounts
- Creación de `CustomUserCreationForm` en `forms.py`
- Vista de registro con `UserCreationForm`
- Vista de login con `AuthenticationForm`
- Vista de logout
- Configuración de `LOGIN_URL` y `LOGIN_REDIRECT_URL` en `settings.py`
- Protección de vistas con `@login_required`
- Navbar dinámica según estado de autenticación

##  Estructura

- `core` → home, about y template base
- `categorias` → modelo y CRUD de categorías
- `productos` → modelo y CRUD de productos y lista de compras
- `accounts` → registro, login y logout de usuarios

##  Autor
Matias Drago