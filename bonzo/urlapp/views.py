import hashlib

from django.http import HttpResponseRedirect
from django.shortcuts import render

import validators
from django.urls import reverse

from urlapp.models import URL


def shorten_url(request):
    context = dict()
    if request.method == 'POST':
        original_url = request.POST["url"]
        if len(original_url) and validators.url(original_url):
            short_url = get_short_url(original_url)
            url_obj = URL(
                origin=original_url,
                short=short_url
            )
            url_obj.save()
            context['short_url'] = short_url
            return render(request, 'urlapp/url.html', context)
        else:
            # return render(request, 'mainapp/index.html', context)
            return HttpResponseRedirect(reverse('mainapp:index'))


def get_short_url(url: str):
    hash_object = hashlib.sha1(url.encode())
    short_url = hash_object.hexdigest()[10:18]
    return short_url
