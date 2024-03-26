from django.db import models





class Verification(models.Model):
   
    telefone = models.CharField(max_length = 15, blank=True, null=True)
    codigo = models.CharField(max_length = 15, blank=True, null=True)
