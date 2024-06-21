from uuid import uuid4
from datetime import date

from django.db import models

from accounts.models import Users


class Tasks(models.Model):
    status_options = (
        ('SUCCESS', 'SUCCESS'),
        ('PENDING', 'PENDING')
    )
    
    id = models.UUIDField(primary_key=True, editable=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    due_date = models.DateField(default=date.today)
    status = models.CharField(max_length=20, choices=status_options, default='PENDING')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_tasks')
    
