from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, DeleteView, CreateView
from django.http import HttpResponse
from .models import Book, Company
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
# Create your views here.

class HellowWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>fuck off</h1>')
    
class Templateview(TemplateView):
    template_name='clsapp/test.html' 

class TemplateViewContext(TemplateView):
    template_name='clsapp/test.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Nagarjuna'
        context['city']='Banglore'
        context['sex']='Male'
        context['girl_friend']='Sunny'
        return context

class BookListView(ListView):
    model=Book
    template_name='clsapp/book_list.html'
    # default page: book_list.html

class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields=['name', 'location', 'ceo']

class CompanyUpdateView(UpdateView):
    model=Company
    fields=['name', 'ceo']

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('company_list')
