
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path(
        'videojuegos/',
        views.videojuegos,
        name='videojuegos'
    ),

    path(
        'motos/',
        views.lista_motos,
        name='lista_motos'
    ),

    path(
        'motos/crear/',
        views.crear_moto,
        name='crear_moto'
    ),

    path(
        'motos/editar/<int:moto_id>/',
        views.editar_moto,
        name='editar_moto'
    ),

    path(
        'motos/eliminar/<int:moto_id>/',
        views.eliminar_moto,
        name='eliminar_moto'
    ),

]
