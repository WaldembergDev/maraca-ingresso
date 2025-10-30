from django.shortcuts import render
from ingressos.models import Ingresso

# Create your views here.
def home(request):
    if request.method == 'GET':
        ingressos = Ingresso.objects.filter()
        context = {
            'igressos': ingressos
        }
        return render(request, 'core/home.html', context)