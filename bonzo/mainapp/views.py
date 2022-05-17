from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'главная',
    }
    print(context)
    return render(request, 'mainapp/index.html', context)


def get_short_url(request):
    if request.method == 'POST':
        short_url = request.POST["url"]
        context = {
            'short_url': short_url
        }
        return render(request, 'mainapp/url.html', context)
