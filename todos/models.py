from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __st__(self):
        return self.title