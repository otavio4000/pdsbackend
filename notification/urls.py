from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('notifications/<int:pk>/', views.UserNotificationListView.as_view(), name='user-notification-list-view'),
    path('notifications/edit/', views.UserNotificationUpdateSeenView.as_view(), name='user-notification-update-seen-view'),
    path('notifications/email/', views.EmailAPI.as_view(), name='send-email'),
    
]

urlpatterns += staticfiles_urlpatterns()