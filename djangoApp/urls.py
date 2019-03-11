from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
url(r'^connect/(?P<operation>,+)/(?P<pk>\d+)/ $',views.change_member,name="change_memebr")
]
