from django.shortcuts import render
from django.views import generic
from .models import Event
from .forms import EventForm
from django.urls.base import reverse_lazy
from rest_framework import viewsets, generics
from .serializers import EventSerializer

# Create your views here.

class IndexView(generic.ListView):
    template_name="events_list.html"
    context_object_name = 'events'
    def get_queryset(self):
        return Event.objects.all()


class DetailView(generic.DetailView):
    model = Event
    template_name="events_detail.html"


class CreateView(generic.CreateView):
    form_class = EventForm
    model = Event
    template_name = "events_create.html"


class UpdateView(generic.UpdateView):
    form_class = EventForm
    model = Event
    template_name = "events_update.html"



class DeleteView(generic.DeleteView):
    model = Event
    template_name = "events_delete.html"
    success_url = reverse_lazy('create_view')


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventCreate(generics.CreateAPIView):
    serializer_class = EventSerializer


class EventDestroy(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUpdate(generics.UpdateAPIView):
    queryset = Event.objects.all()
    lookup_field = 'pk'
    serializer_class = EventSerializer
