from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('create-task/', create_task_view, name='create_task_url'),
    path('delete-task/<int:pk>/', delete_task_view, name='delete_task_url'),
    path('update-status/<int:pk>/', update_status_view, name='update_status_url'),
    path('deleted/', deleted_view, name='deleted_tasks_url'),
    path('finished/', finished_view, name='finished_tasks_url'),
    path('in-progress/', in_progress_view, name='inprogress_tasks_url'),
]