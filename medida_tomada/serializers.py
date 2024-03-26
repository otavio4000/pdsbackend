from rest_framework import serializers
from .models import MedidaTomada

class MedidaTomadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedidaTomada
        fields = '__all__'