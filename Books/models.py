from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Books(models.Model):
    title = models.TextField(max_length=120, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    author = models.TextField(max_length=60)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
