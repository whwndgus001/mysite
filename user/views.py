from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import user.models as usermodels


def joinform(request):
    return render(request, 'user/joinform.html')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def join(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']

    usermodels.insert(name, email, password, gender)
    return HttpResponseRedirect('/user/joinsuccess')

def loginform(request):
    return render(request, 'user/loginform.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    result = usermodels.fetchone(email, password)
    if result is None:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # login 처리
    request.session['authuser'] = result;


    return HttpResponseRedirect('/')

def logout(request):
    del request.session['authuser']
    return HttpResponseRedirect('/')