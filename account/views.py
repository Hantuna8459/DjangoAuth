from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='')
def homepage_view():
    return render ()

def login_view(request):
    if request.method == 'POST':
        username = request.POST('username') or request.POST('email')
        password = request.POST('password')
        
        user = authenticate(username=username, password=password, email=username)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "There Was An Error Logging In, Please Try Again...")
            form = AuthenticationForm()
    context = {'form':form}
    return render (request, context)

def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
 
@login_required(login_url='')        
def logout_view():
    return redirect ('')