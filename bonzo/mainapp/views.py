from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'главная',
    }
    print(context)
    return render(request, 'mainapp/index.html', context)


def sh_url(request, short_url):
    context = {
        'page_title': short_url,
    }
    return render(request, 'mainapp/index.html', context)


def duplicate_short_url_check():
    pass


def duplicate_url_check():
    pass


def get_short_url():
    pass
