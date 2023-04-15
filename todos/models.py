from django.db import models

# Create your models here.

class Todo_Entity(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    createdAt = models.DateTimeField()

