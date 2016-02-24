from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    (r'generic/$', views.generic),
)
