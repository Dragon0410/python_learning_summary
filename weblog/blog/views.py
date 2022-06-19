from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django import views

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'index.html'