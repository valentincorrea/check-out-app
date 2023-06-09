from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('computers')
        else:
            messages.success(request, ('Username or password is incorrect, try again'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {'navbar':'login'})


def logout_user(request):
    logout(request)
    messages.success(request, ('You were logged out'))
    return redirect('home')


