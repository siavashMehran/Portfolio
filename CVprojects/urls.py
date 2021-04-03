from CVprojects.views import projects, projectDetailView
from django.urls import path

urlpatterns = [
    path('projects', projects),
    path('projects/<str:slug>', projectDetailView)
]
