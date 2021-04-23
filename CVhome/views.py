
from CVabout.models import AboutMe
from CVhome.models import Home
from django.shortcuts import render

def home(request):

    info    = Home.objects.earliest('pk')
    aboutMe = AboutMe.objects.earliest('pk')
    context = {
        'info'  : info,
        'about' : aboutMe
    }
    return render(request, 'index.html', context)