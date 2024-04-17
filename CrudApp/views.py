from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Item

# Create your views here.
class ItemCreateView(CreateView):
    model = Item
    fields = ['id', 'item_name', 'description']
    template_name = 'create.html'
    success_url = '/create/'

class ItemListView(ListView):
    model = Item
    template_name = 'view.html'
    context_object_name = 'item_list'

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name', 'description']
    template_name = 'update.html'
    success_url = '/'

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'delete.html'
    success_url = '/'
