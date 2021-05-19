from django.shortcuts import render
from django.utils import timezone

from news.models import New
from events.models import Event

# Create your views here.

def index(request):
    latest_news_list = New.objects.order_by('-publish_date')[:3]
    next_events_list = Event.objects.filter(
            end_date__gte=timezone.now()
        ).order_by('start_date')[:3]

    context = {'latest_news_list': latest_news_list, 'next_events_list' : next_events_list}
    return render(request, 'combi/index.html', context)
