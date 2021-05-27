from django.views import generic
from events.models import Event
from news.models import  New

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'context'

    def get_queryset(self):
        context = {
            'events':Event.objects.all()[:3],
            'news':New.objects.all()[:3]
            }
        return context
