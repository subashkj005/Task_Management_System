from datetime import date

from rest_framework import serializers

from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)
    
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'due_date', 'status']
        extra_kwargs = {
            'id': {'required': False},
            'user': {'required': False}
        }
        
    def validate_title(self, value):
        if Tasks.objects.filter(title__icontains=value):
            raise serializers.ValidationError('Task already exists')
        return value
    
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date must be future date or today's date")
        return value