from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone
from django.http import Http404
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .forms import NewsForm
from .models import New, Event


def index(request):
    latest_news_list = New.objects.order_by('-id')[:3]
    latest_events_list = Event.objects.order_by('-id')[:3]
    context = {
        'latest_news_list': latest_news_list,
        'latest_events_list': latest_events_list,
    }
    return render(request, 'newspaper/index.html', context)


def create_news(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'newspaper/create.html', {'form': form})


def news_view(request):
    news_list = New.objects.order_by("publish_date")
    context = {
        'news_list': news_list,
    }
    return render(request, 'newspaper/news_view.html', context)


def news_view_detail(request, news_id):
    news = New.objects.get(pk=news_id)
    return render(request, 'newspaper/news_view_detail.html', {'news': news})


def news_update(request, news_id):
    news = get_object_or_404(New, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, files=request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_view')
    else:
        form = NewsForm(instance=news, initial={'news_id': news_id})
    return render(request, 'newspaper/news_update.html', {'form': form})


def news_delete(request, news_id):
    news = get_object_or_404(New, pk=news_id)
    if request.method == 'POST':
        news.image.delete()
        news.delete()
        return redirect('news_view')
    return render(request, 'newspaper/news_delete.html')

class NewsCreate(CreateView):
    form_class = NewsForm
    template_name = 'newspaper/create.html'
    success_url = 'create'

    def get_success_url(self):
        return reverse('newspaper:newsCreateClass')
