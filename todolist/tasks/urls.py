from django.urls import path
from django.urls import include, path
from .views import home, add_task, edit_task, delete_task

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
]