from django.db import models

# Create your models here.

class Url(models.Model):
    original_url = models.CharField(max_length=200)


    def __str__(self):
        return self.original_url