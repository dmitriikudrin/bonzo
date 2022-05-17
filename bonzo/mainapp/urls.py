from django.contrib import admin
from django.urls import path, re_path
from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    re_path(r'(?P<short_url>.{8})/$', mainapp_views.sh_url, name='sh_url'),
]
