import hashlib
import random
import string

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
            short_url = get_short_url(5)
            url_obj = URL(
                original=original_url,
                short=short_url
            )
            url_obj.save()
            # context['short_url'] = f'http://bonzzo:8000/{short_url}'
            context['short_url'] = f'http://127.0.0.1:8000/{short_url}'
            return render(request, 'urlapp/url.html', context)
        else:
            # return render(request, 'mainapp/index.html', context)
            return HttpResponseRedirect(reverse('mainapp:index'))


def get_short_url(length: int):
    letters = string.ascii_letters
    short_url = ''
    while True:
        short_url = ''.join(random.choice(letters) for i in range(length))
        if not URL.objects.filter(short=short_url).first():
            break
    return short_url
