from django.urls import path
from . import views

urlpatterns = [
    path('comprar-ingresso/<uuid:id_ingresso>', views.comprar_ingresso, name='comprar_ingresso'),
]
