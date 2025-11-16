from django.urls import path
from . import views

urlpatterns = [
    path('criar-conta/', views.criar_conta_cliente, name='criar_conta_cliente'),
]
