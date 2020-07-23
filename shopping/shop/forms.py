from django import forms

class Home(forms.Form):
    Item_name = forms.CharField()
    Quantity = forms.IntegerField()

class Sign_up(forms.Form):
    f_name = forms.CharField(max_length=30, label='First name', widget=forms.TextInput(attrs={"type":"text", "name":"firstname", "class":"form-control", "id":"firstname", "placeholder":"Enter Firstname",}),)
    l_name = forms.CharField(max_length=30, label='Last name', widget=forms.TextInput(attrs={"type":"text", "name":"laststname", "class":"form-control", "id":"lasttname", "placeholder":"Enter Lastname",}),)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"name":"email", "class":"form-control", "id":"email", "placeholder":"Enter Email",}),)
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class':'form-control','type':'password', 'placeholder':"Enter Password",}),)

class Sign_in(forms.Form):
    user_name = forms.EmailField(label='Email address', widget=forms.TextInput(attrs={'class':'form-control','id':"email", 'placeholder':"Enter Email",}),)
    password =  forms.CharField(label='Password', widget=forms.TextInput(attrs={'class':'form-control','type':'password', 'placeholder':"Enter Password",}),)
