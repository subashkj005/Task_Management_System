from django.urls import path

from tasks import views

urlpatterns = [
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
]