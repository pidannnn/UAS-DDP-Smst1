from django.urls import path
from django.urls import include, path
from .views import home, add_task, edit_task, delete_task, completed_tasks, pending_tasks

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
    path('completed/', completed_tasks, name='completed_tasks'),  # URL tugas selesai
    path('pending/', pending_tasks, name='pending_tasks'),  # URL tugas belum selesai
]