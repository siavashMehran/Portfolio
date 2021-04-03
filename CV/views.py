

from CVhome.models import Home
from django.shortcuts import render


def siteHeaderPartial(request):

    logoUrl = Home.objects.earliest('pk').logo.url

    context = {
        'logoUrl' : logoUrl
    }
    return render(request, 'components/siteheader.html', context)