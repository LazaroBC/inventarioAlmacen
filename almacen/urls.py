from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('listaProductos/', views.listaProductos, name='listaProductos'),
    path('nuevoProducto/', views.nuevoProducto, name='nuevoProducto'),
    path('editarProducto/<int:id>', views.editarProducto, name='editarProducto'),
    path('eliminarProducto/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('mostrarProducto/<int:id>', views.mostrarProducto, name='mostrarProducto'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

