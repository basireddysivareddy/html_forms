from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inserted successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage is inserted seccussfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    topics=Topic.objects.all()
    webpage=Webpage.objects.all()
    d={'webpages':webpage,'topics':topics}
    if request.method=='POST':
        topic=request.POST['topic']
        webpage=request.POST['webpage']
        na=request.POST['na']
        ur=request.POST['ur']
        dt=request.POST['dt']
        T=Topic.objects.ger_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=W,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(topic_name=T,name=na,url=ur,date=dt)[0]
        A.save()

    return render(request,'insert_accessrecords.html')
def select_topic(request):
    topics=Topic.objects.all()
    d={'topics:topics'}

    if request.method=='POST':
        tn=request.POST.getlist('topic')
        print(tn)
        webpages=Webpage.objects.none()
        for i in tn:
            webpages=webpages|Webpage.objects.filter(topic_name=i)
        data={'webpages':webpages}
        return render(request,'display_webpages.html',d)

    return render(request,'select_topic.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'checkbox.html',d)   