from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponsePermanentRedirect


def homepage(request):
    print(request.user.username)
    AllActive = Polls.objects.all()
    context = {
        'AllActive': AllActive
    }
    return render(request, 'polls/index.html', context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        else:
            pass
        return HttpResponsePermanentRedirect(reverse('homepage'))


def logoutView(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse('homepage'))


def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        user = User.objects.create_user(
            username=username,
            first_name=FirstName,
            last_name=LastName,
            email=email,
            password=password)
        user.save()
        print(username, password, FirstName, LastName, email)
    return HttpResponsePermanentRedirect(reverse('homepage'))


def JoinPoll(request, pk):
    tempPoll = Polls.objects.get(id=pk)
    print(request.POST['PollPassword'+str(tempPoll.id)])

    if tempPoll.password == request.POST['PollPassword'+str(tempPoll.id)]:
        return redirect('/pollView/1')
    else:
        return HttpResponsePermanentRedirect(reverse('homepage'))


def pollView(request, pk):

    Title = Polls.objects.get(id=pk)
    AllActive = Question.objects.filter(poll=Title)
    context = {
        'Title': Title.Title,
        'AllActive': AllActive
    }
    return render(request, 'polls/Inpoll.html', context)


def UpVote(request, pk):
    pass


def DownVote(request, pk):
    pass
