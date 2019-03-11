from django.shortcuts import render,redirect
from .models import Task,Team
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, TaskForm
from django.contrib.auth.models import User
@login_required
def home(request):
        if request.method=="POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task=form.save(commit="False")
                task.task_creator = request.user
                taks.save()
                return redirect('home')
        else:
            form = TaskForm()
            users = User.objects.all()
            list=[]

            context={
            'form':form,
            'users':users
            }
            return render(request, 'djangoApp/home.html',context)
def signup(request):
    if request.method=="POST":
             form=SignUpForm(request.POST)
             if form.is_valid():
                 user = form.save()
                 return redirect('home')
    else :
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})
def change_member(request,operation,pk):
     new_member= User.get(pk=pk)
     if operation=='add':
         Team.add_member(request.user,new_member)
     elif operation == 'remove':
         Team.remve_member(request.user,new_member)
     return redirect('home')
