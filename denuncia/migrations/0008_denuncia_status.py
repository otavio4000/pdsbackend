# Generated by Django 5.0.2 on 2024-03-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncia', '0007_denuncia_praticantes_denuncia_titulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='status',
            field=models.CharField(default='nao investigado', max_length=40),
        ),
    ]
