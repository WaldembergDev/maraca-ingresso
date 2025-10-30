from django.shortcuts import render
from ingressos.models import Ingresso

# Create your views here.
def home(request):
    if request.method == 'GET':
        ingressos = Ingresso.objects.all()
        context = {
            'ingressos': ingressos
        }
        return render(request, 'core/home.html', context)