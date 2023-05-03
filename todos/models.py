from django.db import models
import random
# Create your models here.

class userProfile(models.Model):
    name = models.CharField(max_length=20, default="user")

    def __str__(self):
        return self.name
class Todo_Entity(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    done = models.BooleanField(default=False)
    createdAt = models.DateTimeField()
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, default=random.randint(1, 10))

