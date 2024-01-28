from rest_framework.response import Response
from rest_framework.decorators import api_view
from denuncia.models import Denuncia
from .serializers import DenunciaSerializer
from rest_framework import generics 


class DenunciaListView(generics.ListCreateAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
