from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ResponsavelProfile
from .models import Token

class ResponsavelProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = ResponsavelProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profissao', 'endereco', 'telefone', 'dependentes']

class UserAndProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)  # A senha deve ser somente escrita

    profissao = serializers.CharField()
    endereco = serializers.CharField()
    telefone = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        profile_data = {
            'id': user.id,
            'profissao': validated_data.pop('profissao'),
            'endereco': validated_data.pop('endereco'),
            'telefone': validated_data.pop('telefone')
        }
        ResponsavelProfile.objects.create(user=user, **profile_data)
        
        return {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'profissao': profile_data['profissao'],
                'endereco': profile_data['endereco'],
                'telefone': profile_data['telefone']
        }
    
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['token']
