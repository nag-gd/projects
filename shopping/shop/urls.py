from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('list', views.list),
    path('signin/', views.signin),
    path('test/', views.test),

]