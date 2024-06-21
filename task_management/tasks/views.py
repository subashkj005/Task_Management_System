from rest_framework import generics

from .models import Tasks
from .serializers import TasksSerializer


class CreateTaskView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
    
