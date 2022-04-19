from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from .models import New, Event
from .forms import NewsForm
# Create your views here.

def index(request):
    # get news mas recientes
    news =  get_list_or_404(New)
    # get eventos mas recientes
    events = get_list_or_404(Event)


    # add news and events to context
    context = {'news': news, 'events': events}

    return render(request, 'core/index.html', context=context)

def list_news(request):
    # get news
    news = get_list_or_404(New)
    # add news to context
    context = {'news': news}
    return render(request, 'core/list_news.html', context=context)

# lectura de una noticia
def detail_news(request, pk):
    # get news by id
    news = get_object_or_404(New, pk=pk)
    # add news to context
    context = {'news': news}
    return render(request, 'core/detail_news.html', context=context)

# create new news
def create_news(request):
    context ={}

    form = NewsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "core/create_news.html", context)

# delete news
def delete_news(request, pk):
    news = get_object_or_404(New, pk=pk)
    if request.method == 'POST':
        print("llega aqui")
        news.delete()
        return redirect('list_news')
    return render(request, 'core/delete_news.html', context={'news': news})


