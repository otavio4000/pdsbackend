# Generated by Django 5.0.1 on 2024-03-12 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='engajamento_familia',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='situacao_familiar',
            field=models.CharField(max_length=200),
        ),
    ]
