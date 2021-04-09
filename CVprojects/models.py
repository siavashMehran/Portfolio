from django.db import models
from django.db.models.signals import pre_save
import os
from django.http import Http404




def media_upload_path(instance, filepath):

    def get_name_ext(filepath):
        fullName      = os.path.basename(filepath)
        filename, ext = os.path.splitext(fullName)
        return filename, ext
    
    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{filename}{ext}"
    return f"project_images/{instance.title}--{final}"





class ProjectsManager(models.Manager):

    def get_all_active(self):
        return self.get_queryset().filter(isActive=True)

    def getById(self, id):
        item = self.get_queryset().filter(id=id)
        return item.first()

    def getProjectbySlug(self, slug):
        item = self.get_queryset().filter(slug=slug, isActive=True)
        if not item : raise  Http404("Project Does Not Exist ") ;
        else        : return item.first() ;
    def get_most_viewd(self):
        return self.get_queryset().filter(isActive=True).order_by('-views')
 



class CategoryManager(models.Manager):

    def get_related_projects_or_none(self, category:str):

        try:
            qs = self.get_queryset().filter(category=category).first().project_set.all()
            if qs != None:
                qs = qs.order_by('-id')
                return qs

        except:
            return None


class LANGUAGE(models.Model):

    lang = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.lang


class Categories(models.Model):
    
    category = models.CharField(max_length=40)

    objects  = CategoryManager()

    def __str__(self):
        return self.category

    def slugify(self):
        return self.category.replace(" ", "_")

    def get_absoulute_url(self):
        slug = self.slugify()
        return f'/cat/{slug}'




class Project(models.Model):


    title       = models.CharField(max_length=50, blank=False)
    caption     = models.TextField(max_length=700, blank=False)
    slug        = models.SlugField(max_length=20, blank=True, unique=True)
    technology  = models.ManyToManyField(LANGUAGE, blank=True)
    category    = models.ManyToManyField(Categories, blank=True)

    source_code = models.CharField(max_length=200, blank=True)

    imagMain    = models.ImageField(blank=False, upload_to=media_upload_path)

    views    = models.PositiveIntegerField(default=0)
    isActive = models.BooleanField(default=True)

    objects = ProjectsManager()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/projects/{self.slug}"

    def viewsPlusOne(self):
        if self:
            self.views = self.views + 1
            self.save()
        else: return None

    def get_project_techs(self):
        if self : techs = self.technology.all() ;
        else    : return None
        return techs

    


    


def project_pre_save_reciever(sender, instance, *args, **kwargs):
    
    if not instance.slug:
        instance.slug = instance.title.replace(' ', '-')


pre_save.connect(project_pre_save_reciever, sender=Project)


