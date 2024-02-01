from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics 
from .models import Denuncia
from .serializers import DenunciaSerializer

#Cria uma denuncia e pega a lista de denuncias
class DenunciaCreateListView(generics.ListCreateAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

#Pega o id da denuncia e retorna os dados da denuncia
class DenunciaRetrieveView(generics.RetrieveAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer