from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.task_list, name='task-list'),
    path('task-detail/<int:pk>/', views.task_detail, name='task-detail')
]
