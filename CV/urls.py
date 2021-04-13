
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from CV import settings
from .views import sidebarPartial, siteHeaderPartial

urlpatterns = [
    path('admin/', admin.site.urls),

    #render-partial parts
    path('partial/header', siteHeaderPartial, name='siteHeaderPartial'),
    path('partial/sidebar', sidebarPartial, name='sidebarPartial'),

    #apps URLs
    path('', include('CVhome.urls')),
    path('', include('CVcontact.urls')),
    path('', include('CVprojects.urls')),
    path('', include('CVabout.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
