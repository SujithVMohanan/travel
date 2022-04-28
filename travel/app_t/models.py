from django.db import models


# Create your models here.

class Places(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='place_pics')
    decs = models.TextField()

    def __str__(self):
        return self.name
