from django.db import models
from django.utils.timezone import now


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    start = models.DateTimeField(default=now)
    end = models.DateTimeField()

    def __str__(self):
        return self.title
