from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pollView/<str:pk>', views.pollView, name='pollView'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('JoinPoll/<str:pk>', views.JoinPoll, name='JoinPoll'),
    path('UpVote/<str:pk>/<str:pid>/', views.UpVote, name='UpVote'),
    path('CreatePoll', views.CreatePoll, name='CreatePoll'),
    path('DownVote/<str:pk>/<str:pid>/', views.DownVote, name='DownVote'),
    path('AddQuestion/<str:pk>/', views.AddQuestion, name='AddQuestion'),

]
