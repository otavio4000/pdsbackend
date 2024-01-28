from django.urls import path
from . import views

urlpatterns = [
    path('denuncia/', views.DenunciaCreateListView.as_view()),
]