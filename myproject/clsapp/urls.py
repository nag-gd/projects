"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from django.contrib.auth import views
from . import views as iv



urlpatterns = [
    path('view/',iv.HellowWorldView.as_view()),
    path('templateview/',iv.Templateview.as_view()),
    path('templateviewcontext/',iv.TemplateViewContext.as_view()),
    path('booklist/',iv.BookListView.as_view()),
    path('companylist/',iv.CompanyListView.as_view(), name='company_list'),
    re_path(r'update/(?P<pk>\d+)/',iv.CompanyUpdateView.as_view()),
    re_path(r'detail/(?P<pk>\d+)/',iv.CompanyDetailView.as_view(), name='detail'),
    re_path(r'delete/(?P<pk>\d+)/',iv.CompanyDeleteView.as_view(), name='delete'),
    path('create/',iv.CompanyCreateView.as_view()),
    
]
