from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Almacen)
admin.site.register(Producto)

# supersusuario admin
# correo: admin@admin.com
# contraseña: admin
