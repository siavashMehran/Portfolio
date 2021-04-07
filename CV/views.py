

from CVprojects.models import Categories, Project
from CVhome.models import Home
from django.shortcuts import render


def siteHeaderPartial(request):
    
    logoUrl = Home.objects.earliest('pk').logo.url

    context = {
        'logoUrl' : logoUrl
    }
    return render(request, 'components/siteheader.html', context)


def sidebarPartial(request):
    categories  = Categories.objects.all()
    mostViewd   = Project.objects.get_most_viewd()[:3]

    context = {
        'categories' :  categories,
        'most_view'  : mostViewd,
    }
    return render(request, 'components/sidebar.html', context)