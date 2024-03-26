from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

#Responsaveis conseguem acessar esse endpoint
class AlunoListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

#Responsaveis conseguem acessar esse endpoint
class AlunoRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDestroyView(generics.DestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunosDoResponsavelListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # Obtenha o responsavel atualmente logado
        
        responsavel_profile = self.request.user.responsavelprofile # Supondo que o usuário atual seja o responsavel

        # Filtrar todos os alunos associados a esse responsavel
        alunos = Aluno.objects.filter(responsaveis=responsavel_profile)

        # Serialize os alunos e retorne a resposta
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)