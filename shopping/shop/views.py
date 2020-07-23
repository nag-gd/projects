from django.shortcuts import render
from . import forms

# Create your views here.
# def home(request):
#     form = forms.Home()
#     if request.method == 'POST':
#         item = request.POST['Item_name']
#         qunt = request.POST['Quantity']
#         request.session[item] = qunt     # Dictionary items
#         request.session.set_expiry(120)
#     return render(request, 'ss.html', {'form':form})


def home(request):
    return render(request, 'index.html')

def list(request):
    return render(request, 'list.html')

def signin(request):
    l_form = forms.Sign_in(auto_id=False)
    s_form = forms.Sign_up()
    return render(request, 'signin.html', {'l_form':l_form, 's_form':s_form, })

def test(request):
    return render(request, 'test2.html')