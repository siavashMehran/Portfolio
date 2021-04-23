from django.db import models

# Create your models here.

class Home(models.Model):

    logo     =  models.ImageField(upload_to='images/')

    #site title and lil grey txt
    title    = models.TextField(max_length=80, blank=True)
    grey     = models.TextField(max_length=80, blank=True)

    #MY name & title
    name     = models.CharField(max_length=20)
    myTitle  = models.CharField(max_length=20)

    def __str__(self):
        return 'HOME PGAE INFO'