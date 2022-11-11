from django.shortcuts import render

from landing.models import Site


def landing_home(request):
    site = Site.objects.get()
    context = {
        "site": site,
        "title": "Home"
    }
    return render(request, 'landing/index.html', context)
