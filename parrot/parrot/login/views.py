from django.shortcuts import render
from . import forms
from django.core.exceptions import ValidationError

# Create your views here.

def loginform(request):

    form1 = forms.Signin()

    return render(request, 'login/index.html', {'signin_fields' : form1})


def signup(request):

    form = forms.Signin()
    return render(request, 'login/sample.html', {'signin_fields' : form})

def dam(request):

    form = forms.Valid()
    return render(request, 'login/sample2.html', {'signin_fields' : form})