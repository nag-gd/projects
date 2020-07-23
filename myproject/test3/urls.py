from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.teacher_view),
    # path('post/', views.post_view),
    path('post/', views.Post_list.as_view()),
    path('sendmail/', views.send_email_view),
    re_path(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>\w+)/', views.post_detail_view, name='detail_post'),

]