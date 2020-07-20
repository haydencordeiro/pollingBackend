from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('SignUp', views.SignUp, name='SignUp'),
]
