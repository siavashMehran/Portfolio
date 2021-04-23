from django.db import models

# Create your models here.

class Skills(models.Model):


    skill   = models.CharField(max_length=40, blank=False)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return self.skill

class AboutMe(models.Model):

    
    #site intro
    bigImg   = models.ImageField(upload_to='images/')
    p1       = models.TextField(max_length=600)
    p2       = models.TextField(max_length=600)
    slang    = models.CharField(max_length=300)

    def __str__(self):
        return "About me Info"