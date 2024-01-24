from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDenuncia),
    path('denuncia/', views.addDenuncia)
]