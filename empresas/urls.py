from django.urls import path
from . import views

urlpatterns = [
    path("registrar/", views.registrar_empresa, name="registrar_empresa"),
    path("lista/", views.lista_empresas, name="lista_empresas"),
]
