from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    deadline = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title