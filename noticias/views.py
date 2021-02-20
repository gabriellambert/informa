from django.shortcuts import render
from .models import Noticia

def index(request):
    noticias = Noticia.objects.order_by('-data_publicacao').filter(publicada=True)
    dados = {
        'noticias': noticias,
    }
    return render(request, 'index.html', dados)

def noticia(request):
    return render(request, 'noticia.html')
