from django.urls import path
from . import views

urlpatterns = [
    path('comprar-ingresso/<uuid:id_ingresso>', views.comprar_ingresso, name='comprar_ingresso'),
    path('visualizar-ingresso/<uuid:id_ingresso>', views.visualizar_ingresso, name='visualizar_ingresso'),
    path('cadastrar-ingresso/', views.cadastrar_ingresso, name='cadastrar_ingresso')
]
