from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('responsavel/create', views.ResponsavelProfileCreateView.as_view(), name='responsavel-profile-create-view'),
    path('responsavel/<int:pk>/', views.ResponsavelProfileRetrieveView.as_view(), name='responsavel-profile-retrieve-view'),
    path('responsavel/associate/<int:pk>/', views.AssociateDependenteView.as_view(), name='responsavel-associate-dependente-view'),
    path('responsavel/token', views.TokenGenerationView.as_view(), name='responsavel-token'),
    path('responsavel/token/validate', views.TokenValidationView.as_view(), name='responsavel-token-validate'),
    
]

urlpatterns += staticfiles_urlpatterns()