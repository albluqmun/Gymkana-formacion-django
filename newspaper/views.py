from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import BaseItems, New, Event

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "newspaper.html"

class NewView(TemplateView):
    model = New
    template_name = "newspaper/new.html"

class EventView(TemplateView):
    model = Event
    template_name = "newspaper/event.html"