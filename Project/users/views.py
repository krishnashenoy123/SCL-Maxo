from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from .utils import email_check
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import pyrebase


def user_login(request):
    if request.POST:
        user_cred = request.POST['username']
        password = request.POST['password']
        if email_check(user_cred):
            username = User.objects.get(email=user_cred).username
            user = authenticate(request, username=username, password=password)
        else:
            user = authenticate(request, username=user_cred, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged into your account!!')
            return redirect('focus-home')

        else:
            messages.error(request, 'Invalid Credential')
            return redirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'users/login.html', {'title': "Login"})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account has been updated !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/profile.html',context)

def upload(request):
    config={
            'apiKey': "AIzaSyDLzBjNqg37fRiCBClXzamhjdVN2jr4nX8",
            'authDomain': "fir-9f329.firebaseapp.com",
            'databaseURL':"https://fir-9f329.firebaseio.com",
            'projectId': "fir-9f329",
            'storageBucket': "fir-9f329.appspot.com",
            'messagingSenderId': "1022042387286",
            'appId': "1:1022042387286:web:efbafb88c136023dd0dcf7",
            'measurementId': "G-F8NR0833P8"
            }
    firebase= pyrebase.initialize_app(config)
    storage=firebase.storage()
    path_local= input("enter name of file")
    
    path_on_cloud=input("enter the file on cloud")
    storage.child(path_on_cloud).put(path_local)
    Url=storage.child(path_on_cloud).get_url(None)
    print(Url)

def displays(request):
    pass
    #display all the file in the main firbase directory
    #when you click on the link it should lead to subdirectories

