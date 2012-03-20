from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Task(models.Model):
    """Models an individual task"""
    user = models.ForeignKey(User)
    text = models.TextField()
    complete = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now())
