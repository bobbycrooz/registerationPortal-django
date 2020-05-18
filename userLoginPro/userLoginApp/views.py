from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from userLoginApp.form import userRegForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def serverOK(request):
    return render(request, 'websites/serverOK.html',)
    
def index(request):
    return render(request, 'websites/index.html',)

@login_required
def special(request):
    return HttpResponse('login successful')

@login_required
def logout_success(request):
    logout(request)
    return HttpResponseRedirect(reverse('websites:home'))

def userLogin(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user :
            if user.is_active :
                login(request, user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse('you are not active')
        else:
            return HttpResponse('Your are not a member')

    else:
        return render(request, 'websites/login.html', {})






#begin registration form script
def register(request):

    registered = False

    if request.method == 'POST' :
        form = userRegForm(data=request.POST)

        if form.is_valid():

            user = form.save()
            user.save()

            registered = True
        else:
            print(form.errors)
    else:
        form = userRegForm()

    return render(request, 'websites/registration.html', { 'form' : form, 'registered': registered })

