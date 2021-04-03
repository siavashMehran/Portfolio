
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from CV import settings
from .views import siteHeaderPartial

urlpatterns = [
    path('admin/', admin.site.urls),

    #render-partial parts
    path('partial/header', siteHeaderPartial, name='siteHeaderPartial'),

    #apps URLs
    path('', include('CVhome.urls')),
    path('', include('CVcontact.urls')),
    path('', include('CVprojects.urls')),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
