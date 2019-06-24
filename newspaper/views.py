
from django.shortcuts import render, loader

# Create your views here.
from django.utils import timezone
from .models import New, Event


def index(request):
    latest_news_list = New.objects.order_by('-id')[:3]
    latest_events_list = Event.objects.order_by('-id')[:3]
    context = {
        'latest_news_list': latest_news_list,
        'latest_events_list': latest_events_list,
    }
    return render(request, 'newspaper/index.html', context)
