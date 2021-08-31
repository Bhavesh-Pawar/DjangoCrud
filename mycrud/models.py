from django.db import models

# Create your models here.

class Info(models.Model):
    name=models.CharField(max_length=35)
    contact=models.CharField(max_length=32)

    def __str__(self):
        return self.name
    