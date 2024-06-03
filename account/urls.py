from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#create urls here

urlpatterns = [
   path('', views.login_view, name='login'),
   path('register/', views.register_view, name='register'),
   path('activate/', views.email_send, name=''),
   path('home/', views.homepage_view, name='home_page'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
]
