from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
# installed
from ipware import get_client_ip


def homepage(request):
    ip, is_routable = get_client_ip(request)

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

    ip, is_routable = get_client_ip(request)
    tempPoll = Polls.objects.get(id=pk)
    UsersName = request.POST['UsersName'+pk]

    if tempPoll.password == request.POST['PollPassword'+str(tempPoll.id)]:
        tempUser = UserModel(Name=UsersName,
                             Ip=ip,
                             CurrentPoll=tempPoll
                             )
        tempUser.save()
        return redirect('/pollView/'+str(pk))
    else:
        return HttpResponsePermanentRedirect(reverse('homepage'))


def CreatePoll(request):

    poll = Polls(UniqueId=request.POST['uid'],
                 Title=request.POST['PollTitle'],
                 Description=request.POST['PollDesc'],
                 password=request.POST['Pollpassword'],
                 Author=request.user)
    poll.save()
    return HttpResponsePermanentRedirect(reverse('homepage'))


def pollView(request, pk):
    currentUser = UserModel.objects.filter(
        Ip=get_client_ip(request)[0]).first()
    upvotes = UpvoteLogs.objects.filter(UserFK=currentUser)
    upvotes = [i.Question.id for i in upvotes]
    downvotes = DownvoteLogs.objects.filter(UserFK=currentUser)
    downvotes = [i.Question.id for i in downvotes]

    Title = Polls.objects.get(id=pk)
    AllActive = Question.objects.filter(poll=Title)
    UpVote = []
    for i in AllActive:
        temp = [i]
        if i.id in upvotes:
            temp.append(True)
        else:
            temp.append(False)
        if i.id in downvotes:
            temp.append(True)
        else:
            temp.append(False)

        temp.append(len(UpvoteLogs.objects.filter(Question=i)) -
                    len(DownvoteLogs.objects.filter(Question=i)))
        UpVote.append(temp)
        # print(temp)
    UpVote.sort(key=lambda x: x[3], reverse=True)
    AllActive = UpVote
    # print(UpVote)

    context = {
        'PollId': Title.id,
        'Title': Title.Title,
        'AllActive': AllActive
    }
    return render(request, 'polls/Inpoll.html', context)


def UpVote(request, pk, pid):

    currentUser = UserModel.objects.filter(
        Ip=get_client_ip(request)[0]).first()
    temp = UpvoteLogs(UserFK=currentUser,
                      Question=Question.objects.get(id=pk))
    temp.save()
    return HttpResponseRedirect(f'/pollView/{pid}')


def DownVote(request, pk, pid):
    currentUser = UserModel.objects.filter(
        Ip=get_client_ip(request)[0]).first()
    temp = DownvoteLogs(UserFK=currentUser,
                        Question=Question.objects.get(id=pk))
    temp.save()
    return HttpResponseRedirect(f'/pollView/{pid}')


def AddQuestion(request, pk):

    question = Question(poll=Polls.objects.get(id=pk),
                        QuestionText=request.POST['questionAdd'],
                        User=UserModel.objects.filter(
        Ip=get_client_ip(request)[0]).first()
    )
    question.save()
    return HttpResponseRedirect(f'/pollView/{pk}')


def Backend(request):
    pass
