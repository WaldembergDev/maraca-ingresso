from django.shortcuts import render, redirect
from django.db import transaction, models
from .models import Ingresso, HistoricoCompra
from django.shortcuts import get_object_or_404


# Create your views here.
def comprar_ingresso(request, id_ingresso):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            ingresso = get_object_or_404(Ingresso, pk=id_ingresso)
            try:
                with transaction.atomic():
                    quantidade = form.cleaned_data['quantidade']
                    ingresso_travado = Ingresso.objects.select_for_update().get(pk=id_ingresso)
                    if quantidade > ingresso_travado.estoque_disponivel:
                        raise Exception('Estoque insuficiente para esta compra.')
                    ingresso_travado.estoque_disponivel -= quantidade
                    ingresso_travado.save()

                    cliente = request.user
        
                    HistoricoCompra.objects.create(
                        cliente=cliente,
                        ingresso=ingresso_travado,
                        titulo=ingresso_travado.titulo,
                        local=ingresso_travado.local,
                        valor_pago=ingresso_travado.preco,
                        quantidade=quantidade
                        )
                    return redirect('')
            except Exception as e:
                return render(request, 'erro.html', {'mensagem': str(e)})
    return render(request, 'venda_form.html', {'form': form, 'ingresso': ingresso})

def criar_ingresso(request):
    pass

def visualizar_ingresso(request, id_ingresso):
    ingresso = get_object_or_404(Ingresso, pk=id_ingresso)
    if request.method == 'GET':
        pass
