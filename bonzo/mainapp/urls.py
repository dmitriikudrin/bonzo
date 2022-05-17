from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='index'),
    path('url/', mainapp_views.get_short_url, name='url'),

]
