from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.lista_categorias, name='lista'),
    path('crear/', views.crear_categoria, name='crear'),
]