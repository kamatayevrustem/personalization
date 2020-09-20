from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib.auth.forms import UserCreationForm
# from

def home(request):
    return render(
        request,
        'home.html'
    )

def logged(request):
    print(request)
    return render(
        request,
        'logged_user.html'
    )

def signup(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('home')
    else:
        f = UserCreationForm()

    return render(request, 'signup.html', {'form': f})
