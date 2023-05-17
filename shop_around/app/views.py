from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *



class HomeView(ListView):
    model = Product
    template_name = 'index.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products_4'] = Product.objects.all()[-4:]
        context['pols'] = Pol.objects.all()
        context['sizes'] = Size.objects.all()
        context['galleries'] = Gallery.objects.all()
        return context
    class Meta:
        pass