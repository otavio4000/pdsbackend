from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

class EmailAPI(APIView):
    def get(self, request):
        subject = self.request.GET.get('subject')
        txt = self.request.GET.get('text')
        html = self.request.GET.get('html')
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt is None and html is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html is not None and txt is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html is None and txt is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        print(from_email)
       
        try:
            sent_mail = send_mail(
            subject,
            txt,
            from_email,
            recipient_list.split(','),
            html_message=html,
            fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)
            
        except  Exception as e:
            return Response({'msg': 'Erro ao enviar e-mail: {}'.format(str(e))}, status=500)
            

class UserNotificationListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NotificationSerializer

    def get_queryset(self):
        
        user_pk = self.kwargs.get('pk')

        # Obtenha o usuário com base no pk da URL
        user = get_object_or_404(User, pk=user_pk)


        # Filtrar as notificações do usuário autenticado
        queryset = Notification.objects.filter(user=user)

        return queryset
    
class UserNotificationUpdateSeenView(APIView):
    def post(self, request):
        id_value = request.data.get('id')
        try:
            notification = Notification.objects.get(id=id_value)
            notification.is_read = True
            notification.save()
            return Response(status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)