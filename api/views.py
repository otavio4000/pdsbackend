from rest_framework.response import Response
from rest_framework.decorators import api_view
from denuncia.models import Denuncia
from .serializers import DenunciaSerializer

@api_view(['GET'])
def getDenuncia(request):
    denuncias = Denuncia.objects.all()
    serializer = DenunciaSerializer(denuncias, many = True)
    return Response(serializer.data)

@api_view(['POST'])

def addDenuncia(request):
    serializer = DenunciaSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



