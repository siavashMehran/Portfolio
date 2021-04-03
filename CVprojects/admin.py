from CVprojects.models import Categories, LANGUAGE, Project
from django.contrib import admin

# Register your models here.
admin.site.register(Project)
admin.site.register(LANGUAGE)
admin.site.register(Categories)

# admin.site.register([Categories, LANGUAGE, Project])