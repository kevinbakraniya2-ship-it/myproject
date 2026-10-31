from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-project/', views.add_project, name='add_project'),
    path('edit-project/<int:id>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:id>/', views.delete_project, name='delete_project'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]