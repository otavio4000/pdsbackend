from django.urls import path
from rest_framework_simplejwt import views
from .views import MedidaTomadaCreateView
from .views import MedidasTomadasListAPIView
from .views import MedidaTomadaRetrieveView
from .views import MedidaTomadaUpdateView
urlpatterns = [
    path('medida', MedidaTomadaCreateView.as_view(), name='medida'),
    path('medida/<int:pk>/', MedidaTomadaRetrieveView.as_view(), name='medida-detail-view'),
    path('medida/denuncia/<int:pk>/', MedidasTomadasListAPIView.as_view(), name='medida-denuncia-list-view'),
    path('medida/update/<int:pk>/', MedidaTomadaUpdateView.as_view(), name='medida-update-view'),
]