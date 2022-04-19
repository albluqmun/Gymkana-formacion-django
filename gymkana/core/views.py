from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import New, Event
# Create your views here.

def index(request):
    # get news mas recientes
    news =  get_list_or_404(New)
    # get eventos mas recientes
    events = get_list_or_404(Event)


    # add news and events to context
    context = {'news': news, 'events': events}

    return render(request, 'core/index.html', context=context)
