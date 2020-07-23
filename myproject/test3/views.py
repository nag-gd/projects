from django.shortcuts import render,get_object_or_404
from .models import Teacher,Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.core.mail import send_mail
from test3.forms import Send_email_form
from django.contrib import messages

# Create your views here.

def teacher_view(request):
    teacher=Teacher.objects.sal_range(12,35)
    return render(request,'test3/test.html', {'e':teacher})


# 
# def post_view(request):
#     post_list=Post.objects.all()

#     paginator=Paginator(post_list,1)
#     page_number=request.GET.get('page')
#     try:
#         fuck_page_list=paginator.page(page_number)
#     except PageNotAnInteger:
#         fuck_page_list=paginator.page(1)
#     except EmptyPage:
#         fuck_page_list=paginator.page(Paginator.num_pages)

#     return render(request, 'test3/post_list.html', {'post':fuck_page_list})
 

class Post_list(ListView):
    model=Post
    paginate_by=1



def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request, 'test3/detail_post.html', {'post':post})


def send_email_view(request):
    form=Send_email_form()

    if request.method=='POST':
        subject = request.POST.get('subject',)
        message = request.POST.get('message',)
        to_email = request.POST.get('to_email',)
        from_email = request.POST.get('name',)
        send_mail(subject, message, from_email, [to_email,])
        print(to_email)
            
    return render(request, 'test3/send.html', {'form5':form})