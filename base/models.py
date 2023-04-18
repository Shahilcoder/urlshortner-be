from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.CharField(max_length=255, unique=False)
    short_url = models.CharField(max_length=7, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
