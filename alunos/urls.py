from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('alunos/add', views.AlunoCreateView.as_view(), name='aluno-create-view'),
    path('alunos/', views.AlunoListView.as_view(), name='aluno-list-view'),
    path('alunos/<int:pk>/', views.AlunoRetrieveView.as_view(), name='aluno-detail-view'),
    path('alunos/edit/<int:pk>/', views.AlunoUpdateView.as_view(), name='aluno-detail-view'),
    path('alunos/delete/<int:pk>/', views.AlunoDestroyView.as_view(), name='aluno-detail-view'),
    path('alunos/responsavel/', views.AlunosDoResponsavelListView.as_view(), name='alunos-do-responsavel-view'),
    
]

urlpatterns += staticfiles_urlpatterns()