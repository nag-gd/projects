from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginform ),
    path('signup', views.signup ),
    path('dam', views.dam ),

]