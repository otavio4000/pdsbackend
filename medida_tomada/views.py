from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .models import MedidaTomada
from .serializers import MedidaTomadaSerializer
from rest_framework import generics
from .models import Denuncia
from django.shortcuts import get_object_or_404

class MedidaTomadaCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedidaTomada.objects.all()
    serializer_class = MedidaTomadaSerializer



class MedidaTomadaRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedidaTomada.objects.all()
    serializer_class = MedidaTomadaSerializer


class MedidasTomadasListAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MedidaTomadaSerializer

    def get_queryset(self):
        
        denuncia_id = self.kwargs['pk']
        denuncia = get_object_or_404(Denuncia, pk=denuncia_id)

        medidas_tomadas = MedidaTomada.objects.filter(denuncia_id=denuncia_id)

        return medidas_tomadas
    
class MedidaTomadaUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = MedidaTomada.objects.all()
    serializer_class = MedidaTomadaSerializer