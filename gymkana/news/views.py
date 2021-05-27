from typing import NewType
from django.shortcuts import get_list_or_404, render
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