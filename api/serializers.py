from rest_framework import serializers
from denuncia.models import Denuncia


class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'