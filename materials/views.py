from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from materials.models import Material


# Create your views here.

class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('main:index')
