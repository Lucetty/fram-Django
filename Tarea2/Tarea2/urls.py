"""Tarea2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ORM_Django.views import menu, listarproducto, producto, editarproducto, eliminarproducto, cliente, listarcliente, \
    editarcliente, eliminarcliente, listarfactura, factura, eliminarfactura, editarfactura

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='index'),
    path('producto/', producto, name='producto'),
    path('listarproducto/', listarproducto, name='listarproducto'),
    path('editarproducto/<int:id>/', editarproducto, name='editarproducto'),
    path('eliminarproducto/<int:id>', eliminarproducto, name='eliminarproducto'),

    path('cliente/', cliente, name='cliente'),
    path('listarcliente/', listarcliente, name='listarcliente'),
    path('editarcliente/<int:id>/', editarcliente, name='editarcliente'),
    path('eliminarcliente/<int:id>', eliminarcliente, name='eliminarcliente'),

    path('factura/', factura, name='factura'),
    path('listarfactura/', listarfactura, name='listarfactura'),
    path('editarfactura/<int:id>/', editarfactura, name='editarfactura'),
    path('eliminarfactura/<int:id>', eliminarfactura, name='eliminarfactura'),
]
