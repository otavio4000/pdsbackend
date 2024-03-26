from django.urls import path
from rest_framework_simplejwt import views
from .views import VerificationCreateView
from .views import VerificationCheckView

urlpatterns = [
    path('verification/', VerificationCreateView.as_view(), name='verification'),
    path('verification/check', VerificationCheckView.as_view(), name='check'),
    
]