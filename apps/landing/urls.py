from django.conf.urls import patterns, include, url


handler404 = 'landing.views.custom_404'
handler500 = 'landing.views.custom_404'

urlpatterns = patterns('landing.views',
    url(r'^static/(?P<slug>[-\w]+)/$', 'static_page', name='static_page'),
    url(r'^porto/$', 'porto_list', name='porto_list'),
)
