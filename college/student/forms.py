from django import forms
from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Student
        fields = '__all__'
