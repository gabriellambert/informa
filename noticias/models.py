from django.db import models
from autor.models import Autor
from datetime import datetime

class Noticia(models.Model):
    titulo = models.CharField(max_length=250)
    resumo = models.CharField(max_length=400)
    categoria = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default="")
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
