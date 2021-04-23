from CVabout.models import Skills
from django.http.request import HttpRequest
from django.shortcuts import render
from random import randint
# Create your views here.


def about(request:HttpRequest):
    skills = sorted(Skills.objects.all(), key=lambda x : x.percent + randint(-10, 10), reverse=True)
    context = {
        'skills' : skills
    }
    return render(request, 'about.html', context)