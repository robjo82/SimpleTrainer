"""SimpleTrainer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include, handler404, handler500
from . import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'SimpleTrainer.views.handler404'
handler500 = 'SimpleTrainer.views.handler500'
handler403 = 'SimpleTrainer.views.handler403'
handler400 = 'SimpleTrainer.views.handler400'
views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('a_propos', views.a_propos, name='a_propos'),
    path('bibliotheque/', include('bibliotheque.urls')),
    path('espace_perso/', include('EspacePerso.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    
    path('menu', views.menu, name='menu'),
    #url(r'^test/(?P<id>[0-9]+)$', views.test)
    #re_path('test/(?P<id>[0-9]+)$', views.test)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
