from django.db import models
from denuncia.models import Denuncia




class MedidaTomada(models.Model):
   
    acao = models.CharField(max_length = 200, blank=True, null=True)
    tipo_acao = models.CharField(max_length = 100, blank=True, null=True)
    denuncia_id = models.ForeignKey(Denuncia, on_delete=models.CASCADE)