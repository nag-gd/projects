from django import forms

class Send_email_form(forms.Form):
    name = forms.CharField(max_length=125)
    subject = forms.CharField(max_length=125)
    to_email = forms.EmailField(max_length=125)
    message=forms.CharField(required=False,widget=forms.Textarea)
