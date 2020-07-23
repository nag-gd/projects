from django import forms
from myapp.models import Friends


class AddFriendForm(forms.ModelForm):
 #   name = forms.CharField(max_length=30, label='name', widget=forms.TextInput(attrs={"type":"text", "name":"name", "class":"form-control", "id":"name", "placeholder":"Enter name",}),)
    class Meta:
        model=Friends
        fields='__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=Friends
        fields = '__all__'