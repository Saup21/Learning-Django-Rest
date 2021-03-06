from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.task_list, name='task_list'),
    path('task-detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('task-delete/<int:pk>/', views.task_delete, name='task_delete'),
]
