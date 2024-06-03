from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomRegisterForm
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
 
# Create your views here.

@login_required(login_url='login')
def homepage_view():
    return render ()

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        username_or_email = request.POST.get('username') or request.POST.get('email')
        password = request.POST.get('password')       
        user = authenticate(request, username=username_or_email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")        
    else:
        messages.error(request, "There Was An Error Logging In, Please Try Again...")
    template_name = 'login.html'
    context = {'form':form}
    return render(request, template_name, context)

def register_view(request):
    form = CustomRegisterForm()
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return redirect ('')
    else:
        form = CustomRegisterForm()
    template_name = 'register.html'
    context = {'form':form}
    return render (request, template_name, context)

def email_send(user, request):
    current_site = get_current_site(request)
    subject = 'activate your account'
    message = render_to_string('', {
        'user':user, 
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':default_token_generator.make_token(user),
        })
    return send_mail(subject, message, [user.email])
    
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user - None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success('')
        return redirect('login')
    else:
        messages.info('activation link is invalid!')
        return redirect('login')

# @login_required(login_url='')        
# def logout_view(request):
#     (request)
#     return redirect ('')