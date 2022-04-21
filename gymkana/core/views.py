from multiprocessing import context
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from .models import New, Event
from .forms import NewsForm, EventsForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    context= {}
    # get news mas recientes
    news =  New.objects.all()
    context['news'] = news

    events = Event.objects.all()
    # add news and events to context
    context['events'] = events

    return render(request, 'core/index.html', context=context)

def list_news(request):
    # get news
    news = New.objects.all()
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
    context = {'form': NewsForm()}

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_news')
        else:
            context['form'] = form
    return render(request, 'core/create_news.html', context=context)

# update news
def update_news(request, pk):
    old_news = get_object_or_404(New, pk=pk)
    form = NewsForm(request.POST or None, request.FILES or None, instance=old_news)
    if form.is_valid():
        form.save()
        return redirect('/v1/news/' + str(pk))
    return render(request, 'core/update_news.html', context={'news': old_news, 'form': form})

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
    template_name = 'core/class_list_news.html'
    context_object_name = 'news'

class DetailNews(generic.DetailView):
    model = New
    context_object_name = 'news'
    template_name = 'core/class_detail_news.html'

class CreateNews(generic.CreateView):
    model = New
    form_class = NewsForm
    template_name = 'core/create_news.html'

    success_url = reverse_lazy('class_list_news')

class UpdateNews(generic.UpdateView):
    model = New
    form_class = EventsForm
    template_name = 'core/update_news.html'
    

    def get_success_url(self):
        return reverse_lazy('class_detail_news', kwargs={'pk': self.object.id})


class DeleteNews(generic.DeleteView):
    model = New
    template_name = 'core/delete_news.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy('class_list_news')

### Eventos

class ListEvent(generic.ListView):
    model = Event
    template_name = 'core/list_events.html'
    context_object_name = 'events'

class DetailEvent(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'core/detail_event.html'

class CreateEvent(generic.CreateView):
    model = Event
    fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']
    template_name = 'core/create_event.html'

    success_url = reverse_lazy('list_events')

class UpdateEvent(generic.UpdateView):
    model = Event
    fields = ['title', 'subtitle', 'body', 'start_date', 'end_date']
    template_name = 'core/update_event.html'

    def get_success_url(self):
        return reverse_lazy('detail_event', kwargs={'pk': self.object.id})

class DeleteEvent(generic.DeleteView):
    model = Event
    template_name = 'core/delete_event.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy('list_events')