from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Friends
from myapp.forms import AddFriendForm, UserUpdateForm


@login_required
def home(request):
    return render(request,'myapp/home.html')

@login_required
def friends(request):
    friends_list = Friends.objects.all() # its common error
    return render(request, 'myapp/friends.html', {'friends_list':friends_list})

@login_required()
def add_friend(request):
    form = AddFriendForm() # refresh the form
    if request.method=='POST':
        form = AddFriendForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UserUpdateForm(None)

    return render(request, 'myapp/add_friend.html', {'a_form':form}) 

@login_required()
def del_friend(request,id):
    friend_by_id = Friends.objects.get(id=id)
    friend_by_id.delete()
    return redirect('/friends')

@login_required()
def update_friend(request, id):
    frid = Friends.objects.get(id=id)
    if request.method=='POST':
        form = UserUpdateForm(request.POST, instance=frid)
        if form.is_valid():
            form.save()
            #form = UserUpdateForm(None)
        return redirect('/friends')
    return render(request, 'myapp/update_friend.html', {'f':frid})
