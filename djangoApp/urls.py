from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path(r'^connect/(?P<operation>,+)/(?P<pk>\d+)/$',views.change_member,name='change_member'),
path('team/',views.team,name='team'),
url(r'^task/(?P<pk>\d+)/comment/$', views.add_comment,name='add_comment'),
]
