from CVprojects.views import projects, projectDetailView, search
from django.urls import path

urlpatterns = [
    path('projects', projects),
    path('cat/<str:cat>', search),
    path('projects/<str:slug>', projectDetailView)
]
