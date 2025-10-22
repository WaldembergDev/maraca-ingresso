from django.shortcuts import render
from django.db import transaction
from .models import Ingresso, HistoricoCompra

# Create your views here.
def vender_ingresso(request):
    with transaction.atomic():
        pass
