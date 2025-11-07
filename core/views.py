from django.shortcuts import render, redirect
from ingressos.models import Ingresso
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'GET':
        ingressos = Ingresso.objects.all()
        context = {
            'ingressos': ingressos
        }
        return render(request, 'core/home.html', context)

def login(request):
    # if request.method == ''
    # user = authenticate(username=)
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form': form
        }
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha')
            user = authenticate(request, email=email, senha=senha)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'E-mail ou senha inválidos.')
    
    return render(request, 'core/login.html', context=context)