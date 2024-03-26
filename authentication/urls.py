from django.urls import path
from rest_framework_simplejwt import views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('authentication/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/', views.TokenVerifyView.as_view(), name='token_verify'),
]