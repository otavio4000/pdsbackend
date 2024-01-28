from django.urls import path
from . import views

urlpatterns = [
    path('denuncia/', views.DenunciaCreateListView.as_view(), name='denuncia-create-list-view'),
    path('denuncia/<int:pk>/', views.DenunciaRetrieveView.as_view(), name='denuncia-detail-view'),
]