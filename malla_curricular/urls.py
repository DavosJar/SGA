from django.urls import path, include
from malla_curricular.views import CrearCarrera

urlpatterns = [
    path('crear_carrera/', CrearCarrera)
]
