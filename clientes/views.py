from django.shortcuts import render, redirect
from .forms import ClienteForm
from core.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Create your views here.
def criar_conta_cliente(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        custom_user_form = CustomUserForm(request.POST)
        if cliente_form.is_valid() and custom_user_form.is_valid():
            password = custom_user_form.cleaned_data.get('password')
            usuario = custom_user_form.save(commit=False)
            cliente = cliente_form.save(commit=False)
            usuario.set_password(password)
            cliente.usuario = usuario
            usuario.save()
            cliente.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('criar_conta_cliente')
    else:
        cliente_form = ClienteForm()
        custom_user_form = CustomUserForm()
    context = {
        'cliente_form': cliente_form,
        'custom_user_form': custom_user_form
    }
    return render(request, 'clientes/criar_conta_cliente.html', context=context)
