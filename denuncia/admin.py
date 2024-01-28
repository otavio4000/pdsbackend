from django.contrib import admin
from denuncia.models import Denuncia

# Register your models here.

@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'relato', 'lugar', 'v_fisica', 'v_verbal', 'bullying', 'assedio', 'recorrencia', 'data_ocorrido']
#Alternativa que faz aparecer tudo podendo mudar os valores: admin.site.register(Denuncia)