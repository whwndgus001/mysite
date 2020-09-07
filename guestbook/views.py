from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import guestbook.models as mysitemodel


def index(request):
    results = mysitemodel.fetchlist()
    data = {'mysitelist': results }
    return render(request, 'guestbook/index.html', data)

def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    mysitemodel.insert(name, password, message)

    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    return render(request, 'guestbook/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    mysitemodel.delete(no, password)

    return HttpResponseRedirect('/guestbook')



