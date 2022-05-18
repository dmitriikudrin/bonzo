from django.shortcuts import render, redirect, get_object_or_404

from urlapp.models import UnknownUserURL, RegisteredUserURL


def page_not_found_view(request, exception):
    print(123)
    return render(request, 'mainapp/404.html', status=404)


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def open_short_url(request, short_url):
    if len(short_url) == 8:
        url_model = UnknownUserURL
    else:
        url_model = RegisteredUserURL
    url = get_object_or_404(url_model, short=short_url)
    # url = url_model.objects.filter(short=short_url).get()
    origin_url = url.origin
    return redirect(origin_url)


def duplicate_short_url_check():
    pass


def duplicate_url_check():
    pass


def get_short_url():
    pass
