from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^Hello/$', views.hello),
    url(r'^dtime/(\d)/$', views.dtime),
    url(r'^templ/(\w+)/$', views.templ),
    url(r'^index/(\w+)/(\w+)/$', views.index, name='spis'),
    url(r'^apple/', include('apple.urls')),
    url(r'^admin/', include(admin.site.urls))
)
