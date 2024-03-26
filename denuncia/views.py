from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Denuncia
from .serializers import DenunciaSerializer
from rest_framework.response import Response

#Cria uma denuncia, não precisa de autenticação
class DenunciaCreateView(generics.CreateAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

#Pega a lista de denuncias, precisa de autenticação e ser admin
class DenunciaListView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

#Pega o id da denuncia e retorna os dados da denuncia, precisa de autenticação e ser admin
class DenunciaRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

#Atualiza a denuncia, precisa de autenticação
class DenunciaUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        
        status = request.data.get('status')
        if status is not None:
            instance.status = status
        
        self.perform_update(serializer)
        return Response(serializer.data)   

#Lista todas as denuncias que os dependentes do usuario estão envolvidos, precisa de autenticação
class DenunciaDependentesListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DenunciaSerializer

    def get_queryset(self):
        # Obtenha todos os alunos associados ao usuário atual
        alunos = self.request.user.responsavelprofile.dependentes.all()

        # Obtenha todas as denúncias associadas aos dependentes como vítimas ou praticantes
        queryset = Denuncia.objects.filter(vitimas__in=alunos) | Denuncia.objects.filter(praticantes__in=alunos)
        return queryset.distinct()
