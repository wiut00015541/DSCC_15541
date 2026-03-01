from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
        )
    STATUS_CHOICES = [
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]
    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='active'
)

    def __str__(self):
        return self.title