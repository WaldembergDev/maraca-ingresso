from django.shortcuts import render
from ingressos.models import Ingresso
from django.contrib.auth import authenticate

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
        return render(request, 'core/login.html')
    else:
        email = request.POST.get('inputEmail')
        senha = request.POST.get('password')
        user = authenticate(request, )