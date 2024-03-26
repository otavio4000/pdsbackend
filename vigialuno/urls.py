"""
URL configuration for vigialuno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('denuncia.urls')),
    path('api/v1/', include('verification.urls')),
    path('api/v1/', include('responsaveis.urls')),
    path('api/v1/', include('medida_tomada.urls')),
    path('api/v1/', include('alunos.urls')),
    path('api/v1/', include('notification.urls')),
    path('api/v1/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
