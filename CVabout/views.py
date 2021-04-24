from django.core.checks.messages import Debug
from CVabout.models import AboutMe, ContactInfo, Skills
from django.http.request import HttpRequest
from django.shortcuts import render
from random import randint
# Create your views here.


def about(request:HttpRequest, *args, **kwargs):
    skills = sorted(Skills.objects.all(), key=lambda x : x.percent + randint(-10, 10), reverse=True)
    about  = AboutMe.objects.earliest('pk')
    info   = ContactInfo.objects.earliest('pk')
    context = {
        'skills' : skills,
        'about'  : about,
        'info'   : info
    }
    return render(request, 'about.html', context)