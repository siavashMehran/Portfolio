
from CVabout.models import AboutMe, ContactInfo
from CVhome.models import Home
from django.shortcuts import render

def home(request):
    homePageData = Home.objects.earliest('pk')
    aboutMe      = AboutMe.objects.earliest('pk')
    contactInfo  = ContactInfo.objects.earliest('pk')
    context = {
        'info'    : contactInfo,
        'about'   : aboutMe,
        'home'    : homePageData
    }
    return render(request, 'index.html', context)