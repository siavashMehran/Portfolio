

from CVgallery.models import SocialAccountPosts
from CVprojects.models import Categories, Project
from CVhome.models import Home, SiteSetting
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
        'instagram'  : False
    }
    
    if (SiteSetting.objects.earliest('pk').is_instagram_feed_active):
        context['instagram'] = True
        instagram_feed = SocialAccountPosts.objects.all()
        context['instagram_posts'] = instagram_feed

    return render(request, 'components/sidebar.html', context)