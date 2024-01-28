from django.urls import path
from . import views

urlpatterns = [
    path('denuncia/', views.DenunciaListView.as_view()),
]