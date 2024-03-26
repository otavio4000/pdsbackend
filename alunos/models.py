from django.db import models
from django.core.validators import FileExtensionValidator

CHOICES = (
        ('yes', 'Sim'),
        ('no', 'Não'),
    )

class Aluno(models.Model):
    
    matricula = models.IntegerField(unique=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateTimeField()
    turma_ano = models.CharField(max_length=100)
    historico_academico = models.FileField(blank=True, upload_to='alunos/historicos', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    historico_faltas = models.IntegerField(default=0)
    observacoes = models.TextField(blank=True)
    contato_substancias_ilicitas = models.CharField(max_length = 10, choices=CHOICES)
    situacao_familiar = models.CharField(max_length=200)
    engajamento_familia = models.CharField(max_length=200)

    def __str__(self):
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}"