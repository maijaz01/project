from django.conf.urls import patterns, include, url
from django.contrib import admin
from idiot import views
from idiot import urls

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^views/', views.indexViews, name='home'),


)
