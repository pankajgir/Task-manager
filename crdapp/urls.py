from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('task-create', views.task_create, name='task-crete'),
    path('task-edit/<int:pk>/', views.edit, name='task-edit'),
    path('task-delete/<int:pk>/', views.delete, name='task-delete'),
    path('t-toggle/<int:pk>/', views.task_toggle_completed, name='task-toggle'),
]
