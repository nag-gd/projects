from django.shortcuts import render
from .import forms

# Create your views here.

def name_view(request):
    form = forms.NameForm()
    return render(request, 'shopping/name.html', {'form':form})

def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = forms.AgeForm()
    return render(request, 'shopping/age.html', {'form':form})

def gf_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = forms.GFForm()
    return render(request, 'shopping/gf.html', {'form':form})

def results(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'shopping/results.html')