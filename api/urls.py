from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-create/', views.task_create, name='task-create'),
    path('task-details/<int:pk>/', views.task_details, name='task-details'),
    path('task-update/<str:pk>/', views.task_update, name='task-update'),
    path('task-delete/<str:pk>/', views.task_delete, name='task-delete'),
]
