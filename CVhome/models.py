from django.db import models

# Create your models here.

class Home(models.Model):

    logo     =  models.ImageField(upload_to='images/')

    #site title and lil grey txt
    title    = models.TextField(max_length=80, blank=True)
    grey     = models.TextField(max_length=80, blank=True)

    #site intro
    bigImg   = models.ImageField(upload_to='images/')
    p1       = models.TextField(max_length=600)
    p2       = models.TextField(max_length=600)
    slang    = models.CharField(max_length=300)

    #social media links
    github   = models.URLField()
    insta    = models.URLField()
    linkedin = models.URLField()

    #MY name & title
    name     = models.CharField(max_length=20)
    myTitle  = models.CharField(max_length=20)

    def __str__(self):
        return 'HOME PGAE INFO'