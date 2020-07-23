from django.shortcuts import render
from . import forms
from student.models import Student


# Create your views here.

def index_view(request): 
    return render(request, 'student/index.html')
    
def sample(request):
    return render(request, 'student/sample.html')

def add_student(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('data saved successfully')
    return render(request, 'student/add_data.html', {'form':form})

def student_list(request):
    list = Student.objects.all()
    counter = int(request.session.get('count', 0))
    newcount =counter+1
    response = render(request, 'student/list_data.html', {'list':list, 'count':counter})
    request.session['count'] =  newcount
    return response