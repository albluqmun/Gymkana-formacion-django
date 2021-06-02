from typing import NewType
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls.base import reverse_lazy
from django.views import generic
from django.urls import reverse
from .models import New
from .forms import NewForm


def index(request):
    news = New.objects.all()
    return render(request, 'list.html', {'news':news})


def create(request):
    new_form = NewForm(request.POST or None, request.FILES or None)
    if new_form.is_valid():
        instance_new = new_form.save(commit=False)
        instance_new.save()
        return HttpResponseRedirect(reverse('news:detail', args=[instance_new.id]))
    return render(request, 'create.html', {'form':new_form})


def detail(request, id):
    new = get_object_or_404(New, id = id)
    return render(request, 'detail.html', {'new': new})


def update(request, id):
    new = get_object_or_404(New, id = id)
    updated_form = NewForm(request.POST or None, request.FILES or None, instance = new)
    if updated_form.is_valid():
        updated_form.save()
        return HttpResponseRedirect(reverse('news:detail',  args=[id]))
    return render(request, 'new_update.html', {'form':updated_form})

def delete(request, id):
    new = get_object_or_404(New, id = id).delete()
    return HttpResponseRedirect(reverse('news:index'))


class IndexView(generic.ListView):
    template_name="list.html"
    context_object_name = 'news'
    def get_queryset(self):
        return New.objects.all()


class DetailView(generic.DetailView):
    model = New
    template_name="detail.html"

class CreateView(generic.CreateView):
    model = New
    fields = '__all__'
    template_name = "create.html"

class UpdateView(generic.UpdateView):
    model = New
    fields = '__all__'
    template_name = "update.html"

class DeleteView(generic.DeleteView):
    model = New
    template_name = "delete.html"
    success_url = reverse_lazy('create_view')
