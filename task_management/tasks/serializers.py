from rest_framework import serializers

from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    
    status = serializers.CharField(required=False)
    
    class Meta:
        model = Tasks
        fields = []