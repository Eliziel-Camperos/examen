from django.urls import path 
from Mercancia_app import views
urlpatterns = [
    path("",views.listadomerca,name='listadoMerca')
]
