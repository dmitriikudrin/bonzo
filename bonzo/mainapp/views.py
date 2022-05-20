from django.shortcuts import render, redirect, get_object_or_404

from urlapp.models import URL


def page_not_found_view(request, exception):
    return render(request, 'mainapp/404.html', status=404)


def index(request, errors=None):
    print(errors)
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def open_short_url(request, short_url):
    url_model = URL
    url = get_object_or_404(url_model, short=short_url)
    original_url = url.original
    return redirect(original_url)


def duplicate_short_url_check():
    pass


def duplicate_url_check():
    pass


def get_short_url():
    pass
