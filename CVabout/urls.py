from CVabout.views import about
from django.urls import path

urlpatterns = [
    path('about', about, name="aboutPage")
]
