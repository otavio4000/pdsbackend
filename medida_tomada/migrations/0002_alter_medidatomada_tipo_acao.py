# Generated by Django 5.0.1 on 2024-03-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medida_tomada', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidatomada',
            name='tipo_acao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
