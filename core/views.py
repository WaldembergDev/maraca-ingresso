from django.http import HttpResponse
from django.shortcuts import render, redirect
from ingressos.models import Ingresso
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import EmailAuthenticationForm

# Create your views here.
def home(request):
    if request.method == 'GET':
        ingressos = Ingresso.objects.all()
        context = {
            'ingressos': ingressos
        }
        return render(request, 'core/home.html', context)

def login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return HttpResponse('logado com sucesso!')
    else:
        form = EmailAuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'core/login.html', context=context)

def logout(request):
    auth_logout(request)
    return HttpResponse('Usuário deslogado com sucesso!')