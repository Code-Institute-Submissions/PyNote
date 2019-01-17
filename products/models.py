from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name