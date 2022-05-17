from django.urls import path
from urlapp import views as urlapp_views

app_name = 'urlapp'

urlpatterns = [
    path('shorten/', urlapp_views.shorten_url, name='shorten_url'),

]
