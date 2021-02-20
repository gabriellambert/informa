from django.contrib import admin
from .models import Noticia

class Lista_de_Noticias(admin.modelAdmin):
    list_display = ('titulo', 'categoria', 'publicada')
    search_fields = ('titulo',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)

admin.site.register(Noticia, Lista_de_Noticias)
