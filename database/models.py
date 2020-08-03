from django.db import models

# Create your models here.

class impression_store(models.Model):
    impression = models.TextField()
    time = models.TextField()
