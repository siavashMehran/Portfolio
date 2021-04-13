from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.


def about(request:HttpRequest):

    context = {
        
    }
    return render(request, 'about.html', context)