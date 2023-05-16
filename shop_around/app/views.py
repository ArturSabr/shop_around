from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *



class HomeView(ListView):
    model = Product
    template_name = 'index.html'
    class Meta:
        pass