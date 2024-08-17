from django.urls import path
from .import views

urlpatterns = [
    path('clients/',views.ClientList.as_view()),
    path('clients/<int:pk>/',views.ClientDetail.as_view()),
    path('clients/<int:client_id>/projects/',
         views.ProjectList.as_view(), name='client-projects'),
    path('projects/', views.ProjectDetailView.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view()),
    path('users/projects/', views.UserProjectListView.as_view()),
]