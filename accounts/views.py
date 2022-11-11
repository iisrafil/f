from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from landing.models import Site


# Create your views here.


def auth_login(request):
    site = Site.objects.all().first()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('dashboard_home')
        else:
            messages.error(request, 'Wrong username or password! Try again.')
            return redirect('login')


    else:
        form = AuthenticationForm()

    context = {
        'site': site,
        'form': form,
    }
    return render(request, 'dashboard/login.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

