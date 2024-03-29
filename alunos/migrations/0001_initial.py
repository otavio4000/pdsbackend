# Generated by Django 5.0.1 on 2024-03-11 23:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateTimeField()),
                ('turma_ano', models.CharField(max_length=100)),
                ('historico_academico', models.FileField(upload_to='alunos/historicos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('historico_faltas', models.IntegerField(default=0)),
                ('observacoes', models.TextField(blank=True)),
                ('contato_substancias_ilicitas', models.CharField(choices=[('yes', 'Sim'), ('no', 'Não')], max_length=10)),
                ('situacao_familiar', models.CharField(max_length=100)),
                ('engajamento_familia', models.CharField(max_length=100)),
            ],
        ),
    ]
