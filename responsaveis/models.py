from django.db import models
from django.contrib.auth.models import User
from alunos.models import Aluno

class ResponsavelProfile(models.Model):
    #Campos que já estão no modelo de User: username (CPF), first_name, last_name, email, password
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    dependentes = models.ManyToManyField(Aluno, blank=True, related_name='responsaveis')
    profissao = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class Token(models.Model):
    token = models.CharField(max_length=100, unique=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.token
