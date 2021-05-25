from django.views import generic
from .models import Event, New

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'context'

    def get_queryset(self):
        context = {
            'events':Event.objects.all(),
            'news':New.objects.all()
            }
        return context
