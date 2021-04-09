import os
from CVprojects.models import Project
from django.db import models

# Create your models here.

def media_upload_path(instance, filepath):

    def get_name_ext(filepath):
        fullName      = os.path.basename(filepath)
        filename, ext = os.path.splitext(fullName)
        return filename, ext
    
    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{instance}{ext}"
    return f"project_gallery/{instance}--{final}"

class Gallery(models.Model):

    image    = models.ImageField(upload_to=media_upload_path, blank=False)
    project  = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    def __Str__(self):
        return self.project