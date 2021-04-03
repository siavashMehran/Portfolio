from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.


class ContactMe(models.Model):

    name    = models.CharField(max_length=30)
    email   = models.EmailField(max_length=100, blank=False)

    phone   = models.CharField(max_length=18, blank=True)
    messege = models.TextField(max_length=500, blank=False)

    timestamp = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.messege