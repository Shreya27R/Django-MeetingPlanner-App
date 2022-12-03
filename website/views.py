from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting



# Create your views here.

def welcome(request):
    return render(request,'website/welcome.html',{"meetings": Meeting.objects.all()})


# "num_meetings": Meeting.objects.count()}


def date(request):
    return HttpResponse("import date time" + str(datetime.now()))


def about(request):
    return HttpResponse("This is about me : shreya say hello")
