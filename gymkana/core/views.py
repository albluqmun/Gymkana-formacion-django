from multiprocessing import context
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from .models import New, Event
from .forms import NewsForm
from django.views import generic
from django.urls import reverse_lazy
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
        return redirect('list_news')

    context['form']= form
    return render(request, "core/create_news.html", context)

# update news
def update_news(request, pk):
    news = get_object_or_404(New, pk=pk)
    form = NewsForm(request.POST or None, instance=news)
    if form.is_valid():
        form.save()
        return redirect('/v1/news/' + str(pk))
    return render(request, 'core/update_news.html', context={'news': news, 'form': form})


# delete news
def delete_news(request, pk):
    news = get_object_or_404(New, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('list_news')
    return render(request, 'core/delete_news.html', context={'news': news})

### class views
class ListNews(generic.ListView):
    model = New
    template_name = 'core/list_news.html'
    context_object_name = 'news'

class DetailNews(generic.DetailView):
    model = New
    context_object_name = 'news'
    template_name = 'core/detail_news.html'

class CreateNews(generic.CreateView):
    model = New
    fields = ['title', 'subtitle', 'body', 'image']
    template_name = 'core/create_news.html'

class UpdateNews(generic.UpdateView):
    model = New
    fields = ['title', 'subtitle', 'body', 'image']
    template_name = 'core/update_news.html'

    def get_success_url(self):
        return reverse_lazy('detail_news', kwargs={'pk': self.object.id})

class DeleteNews(generic.DeleteView):
    model = New
    template_name = 'core/delete_news.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy('list_news')
