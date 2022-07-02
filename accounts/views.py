from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
               messages.success(request, ("Invalid Credentials"))
               return redirect('login_user')
    else:
        return render(request,'registration/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('dashboard')


# def register_user(request):

#     if request.method == 'POST':

#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('dashboard')

#     else:
#         form = UserCreationForm()
        
#     return render(request,'registration/register.html', {'form': form,})