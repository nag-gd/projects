from django import forms
from django.forms import widgets
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Signin(forms.Form):

    First_name = forms.CharField(label='First name',
                    validators=(validators.MinLengthValidator(10, message='fuck off'),validators.MaxLengthValidator(40) ),  
                    widget=forms.TextInput(attrs={'placeholder': 'First name', 'id': 'fuck', 'class': 'form-control', }),
                    
                    )
    
    Last_name = forms.CharField(label='Last name',  
                    widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control',}))

    Email_address = forms.EmailField(label='Email address',
                    validators=[validators.EmailValidator(message='fuckoff')],  
                    widget=forms.TextInput(attrs={'placeholder': 'Email Address', 'class': 'form-control',}))

    Password = forms.CharField(label='Password',  
                    widget=forms.TextInput(attrs={'placeholder': 'Password', 'class': 'form-control',}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'), ('green', 'Green'), ('black', 'Black'),]

    birth_year = forms.DateField(widget=forms.SelectDateWidget)
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple({'name':'fuck', 'id': 'sucker'}),
        choices=FAVORITE_COLORS_CHOICES,
    )

  

class Signup(forms.Form):

    def name_error(value):
        if value[0] != 'N':
            raise forms.ValidationError('fuckoff')

    Email = forms.CharField(widget=forms.Textarea, validators=[validators.MinLengthValidator(10)])
    # slug = forms.CharField(validators=[validators.validate_slug])
    name = forms.CharField(validators=[name_error])






    # validators---------------------------------------------------



class Valid(forms.Form):    
    data = forms.CharField()


    def clean(self):
        cleaned_data = super().clean()
        input_data = cleaned_data['data']

        if input_data != 'fuck':
            raise forms.ValidationError('fuck')
