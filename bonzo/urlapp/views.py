import hashlib

from django.shortcuts import render

from urlapp.models import UnknownUserURL


def shorten_url(request):
    if request.method == 'POST':
        url = request.POST["url"]
        short_url = get_short_url(url)
        url_obj = UnknownUserURL(
            origin=url,
            short=short_url
        )
        url_obj.save()
        context = {
            'short_url': short_url
        }
        return render(request, 'mainapp/url.html', context)


def get_short_url(url: str):
    hash_object = hashlib.sha1(url.encode())
    short_url = hash_object.hexdigest()[10:18]
    return short_url
