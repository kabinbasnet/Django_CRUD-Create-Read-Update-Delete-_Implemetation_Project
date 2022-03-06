from django.db import models

# Create your models here.


class TODO(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=60)
    is_complete = models.BooleanField()

    def __str__(self):
        return self.title
