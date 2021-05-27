from typing import NewType
from django.shortcuts import get_list_or_404, render
from django.views import generic
from .models import New


# Create your views here.
def index(request):
    news = New.objects.all()
    return render(request, 'list.html', {'news':news})

def create(request):
    return render(request, 'create.html')

def detail(request, id):
    new = New.objects.get(id = id)
    return render(request, 'detail.html', {'new': new})

def update(request, new_id):
    return render(request, 'update.html')

class IndexView(generic.ListView):
    template_name="list.html"
    context = 'news'
    def get_queryset(self):
        return New.objects.all()

"""
class DetailView(generic.DetailView, id):
    template_name="detail.html"
    context = "new"
    def get_queryset(self):
        return New.objects.get(id = id)
""" 
    