from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()

    def __str__(self):
        return self.desc
