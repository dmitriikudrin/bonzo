from django.contrib import admin
from django.urls import path, re_path
from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('404/', mainapp_views.page_not_found_view, name='404'),
    re_path(r'(?P<short_url>.{8})/$', mainapp_views.open_short_url, name='open_short_url'),
]
