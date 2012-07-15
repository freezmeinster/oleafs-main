from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),
    # url(r'^oleafs/', include('oleafs.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^settings/', include('livesettings.urls')),
)
