from django.db import models

class Denuncia(models.Model):
    relato = models.CharField(max_length = 500)
    lugar = models.CharField(max_length = 50)
    v_fisica = models.CharField(max_length = 10)
    v_verbal = models.CharField(max_length = 10)
    bullying = models.CharField(max_length = 10)
    assedio =  models.CharField(max_length = 10)
    recorrencia = models.CharField(max_length = 50)
    data_ocorrido = models.DateTimeField()
    

