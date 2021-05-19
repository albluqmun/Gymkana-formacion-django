from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import New
from .forms import NewForm

def index(request):
    latest_news_list = New.objects.order_by('-publish_date')[:4]
    context = {'latest_news_list': latest_news_list}
    return render(request, 'news/v1/index.html', context)

def detail(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    return render(request, 'news/v1/detail.html', {'new': new})

def create(request):
    context = {}
    form = NewForm(request.POST or None)
    if form.is_valid():
        new = form.save()
        return render(request, 'news/v1/detail.html', {'new': new})

    context['form'] = form
    return render(request, 'news/v1/create.html', context)

def update(request, new_id):
    new = get_object_or_404(New, pk=new_id)

    form = NewForm(request.POST or None, instance=new)
    if form.is_valid():
        new = form.save()
        return render(request, 'news/v1/detail.html', {'new': new})

    return render(request, 'news/v1/update.html', {'form': form})

def delete(request, new_id):
    context = {}
    new = get_object_or_404(New, pk=new_id)
    if request.method == 'POST':
        new.delete()
        return redirect('index-1')

    return render(request, 'news/v1/confirm_delete.html', context)

class IndexView(generic.ListView):
    template_name = 'news/v2/index.html'
    context_object_name = 'latest_news_list'

    def get_queryset(self):
        """
        Return the last three published news (not including those set to be
        published in the future).
        """
        return New.objects.filter(
            publish_date__lte=timezone.now()
        ).order_by('-publish_date')[:4]

class DetailView(generic.DetailView):
    model = New
    template_name = 'news/v2/detail.html'

    def get_queryset(self):
        """
        Excludes any news that aren't published yet.
        """
        return New.objects.filter(publish_date__lte=timezone.now())

class CreateView(generic.edit.CreateView):
    form_class = NewForm
    template_name = 'news/v2/create.html'

    def get_success_url(self):
        return reverse('news:detail', kwargs={'pk': self.object.id})

class UpdateView(generic.edit.UpdateView):
    model = New
    form_class = NewForm
    template_name = 'news/v2/update.html'

    def get_success_url(self):
        return reverse('news:detail', kwargs={'pk': self.object.id})

class DeleteView(generic.edit.DeleteView):
    model = New

    #Saltar plantilla de confirmacion del delete
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('news:index')