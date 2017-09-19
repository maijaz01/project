from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import *


urlpatterns = patterns(
    # Examples:
    url(r'^home/', 'indexViews', name='indexViews'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^views/', views.indexView, name='indexView'),

)
