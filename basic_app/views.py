from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
# from django.core.urlresolvers import reverse   ## [aita ager vertion a silo akhn r kaj kore na]
from django.urls import reverse
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    return render(request,'index.html',{})

@login_required()
def special(request):
    return HttpResponse("you are logged in, nice!")


@login_required()
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('index'))
    return redirect('index')

def registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST or None)
        profile_form = UserProfileInfoForm(request.POST or None)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'registration.html',
                                      {'user_form':user_form,
                                       'profile_form':profile_form,
                                       'registered':registered })





def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')  # input er name='username' disi (login.html page dekhlei hbe)
        password = request.POST.get('password')    # input er password='password'

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('index'))
                return redirect('index')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse('invalid login details supplied!')

    else:
        return render(request, 'login.html', {})




















