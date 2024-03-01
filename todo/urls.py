from django.urls import path
from . import views
from .views import TaskList, RegisterPage, CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
  
    path('register', views.RegisterPage.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('task-reorder/', views.TaskReorder.as_view(), name='task-reorder'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
     path('task-create/', views.TaskCreate.as_view(), name='task-create'),
     path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
      path('task-delete/<int:pk>/', views.DeleteView.as_view(), name='task-delete'),
    # Add other URL patterns as needed
]