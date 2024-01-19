from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.


def display_topic(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())

    d={'topic':QLTO}
    return render(request,'display_topic.html',d)


def insert_topic(request):
    tn=input('enter topic name: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('Topic is inserted')