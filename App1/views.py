from django.contrib import messages
from django.shortcuts import render, redirect
from App1.models import Mail, User


def signUpForm(request):
    return render(request,'signup.html')

def createAccount(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    if username =='' or password == '':
        return render(request, 'signup.html', context={'em': 'UserName & Password can not be Empty'})
    qs= User.objects.filter(username=username)
    if not qs.exists():
        User.objects.create(name=name,username=username, password=password)
        response=render(request,'login.html',context={'sm':'User Account Created Successfully'})
    else:
        response=render(request,'signup.html',context={'em':'User Email-ID Already Exist'})
    return response


def loginForm(request):
    return render(request,'login.html')

def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if username =='' or password == '':
        return render(request, 'login.html', context={'em': 'UserName & Password can not be Empty'})
    qs = User.objects.filter(username=username, password=password)
    if qs.exists():
        request.session['sender'] = username
        request.session['name']=qs[0].name
        response= redirect('emailInbox')
    else:
        response=render(request, 'login.html', context={'em': 'Invalid UserName & Password'})
    return response


def emailInbox(request):
    sender=request.session['sender']
    name = request.session['name']
    emails = Mail.objects.filter(receiver=sender)
    return render(request, 'inbox.html', {'emails': emails,'name':name})


def deleteEmail(request):
    id = request.GET['id']
    qs=Mail.objects.get(id=int(id))
    qs.delete()
    messages.success(request, 'Email deleted successfully.......')
    return redirect('emailInbox')


def sendEmailForm(request):
    sender = request.session['sender']
    return render(request, 'send.html',context={'email':sender})

def sendEmail(request):
    sender = request.session['sender']
    receiver =request.POST['receiver']
    subject = request.POST['subject']
    body = request.POST['body']
    Mail.objects.create(subject=subject, sender=sender, receiver=receiver, body=body)
    messages.success(request, 'Email send successfully..........')
    return redirect('emailInbox')

def displayEmail(request):
    id = request.GET['id']
    qs = Mail.objects.get(id=int(id))
    return render(request, 'display.html', {'qs': qs})

def searchEmail(request):
    email = request.POST['email']
    name = request.session['name']
    emails = Mail.objects.filter(sender=email)
    return render(request, 'inbox.html', {'emails': emails, 'name': name})