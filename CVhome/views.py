
from CVhome.models import Home
from django.shortcuts import render

def home(request):

    info = Home.objects.earliest('pk')

    context = {
        'info' : info
    }
    return render(request, 'index.html', context)