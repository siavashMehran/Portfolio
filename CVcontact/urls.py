from django.urls import path
from .views import contactMe


urlpatterns = [
    path('contact', contactMe)
]
