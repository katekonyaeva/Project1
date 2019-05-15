import os
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from mrt.models import Mrt
from .forms import CreateForm

class MrtList(ListView):
    template_name = 'mrt_list.html'
    model = Mrt
    paginate_by = 10

class MrtCreate(CreateView):
    form_class = CreateForm
    template_name = 'form.html'
    model = Mrt
    success_url = reverse_lazy('mrt_list')

class MrtUpdate(UpdateView):
    form_class = CreateForm
    template_name = 'form.html'
    model = Mrt
    success_url = reverse_lazy('mrt_list')

class MrtDelete(DeleteView):
    template_name = 'delete.html'
    model = Mrt
    success_url = reverse_lazy('mrt_list')
