from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction, models
from .models import Ingresso, HistoricoCompra
from django.shortcuts import get_object_or_404
from .forms import CompraForm, CadastroIngressoForm
from django.contrib import messages
from clientes.models import Cliente

# Create your views here.
def comprar_ingresso(request, id_ingresso):
    ingresso = get_object_or_404(Ingresso, pk=id_ingresso)
    if request.method == 'POST':
        form = CompraForm(request.POST, ingresso=ingresso)
        if form.is_valid():
            try:                
                with transaction.atomic():
                    quantidade = form.cleaned_data['quantidade']
                    ingresso_travado = Ingresso.objects.select_for_update().get(pk=id_ingresso)
                    if quantidade > ingresso_travado.estoque_disponivel:
                        raise Exception('Estoque insuficiente para esta compra.')
                    ingresso_travado.estoque_disponivel -= quantidade
                    ingresso_travado.save()

                    # obtendo o usuário logado
                    usuario = request.user
                    # obtendo o perfil de cliente do usuário logado
                    cliente = Cliente.objects.get(usuario=usuario)
        
                    HistoricoCompra.objects.create(
                        cliente=cliente,
                        ingresso=ingresso_travado,
                        titulo=ingresso_travado.titulo,
                        local=ingresso_travado.local,
                        valor_pago=ingresso_travado.preco,
                        quantidade=quantidade
                        )
                    messages.success(request, 'Obrigado! Seu ingresso foi comprado com sucesso! Aguarde o contato do administrador')
                    return redirect('home')
            except Exception as e:
                messages.error(request, e)
                return redirect('comprar_ingresso', ingresso.id)
                # return render(request, 'erro.html', {'mensagem': str(e)})
    else:
        form = CompraForm()
    context = {
        'form': form,
        'ingresso': ingresso
    }
    return render(request, 'ingressos/comprar_ingresso.html', context=context)

def criar_ingresso(request):
    pass

def visualizar_ingresso(request, id_ingresso):
    ingresso = get_object_or_404(Ingresso, pk=id_ingresso)
    if request.method == 'POST':
        pass
    else:
        context = {'ingresso': ingresso}
    return render(request, '')

def cadastrar_ingresso(request):
    if request.method == 'POST':
        form = CadastroIngressoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingresso cadastrado com sucesso!')
            return redirect('cadastrar_ingresso')
    else:
        form = CadastroIngressoForm()
    context = {
        'form': form
    }
    return render(request, 'ingressos/cadastrar_ingresso.html', context=context)
