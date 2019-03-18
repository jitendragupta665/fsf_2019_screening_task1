from django.shortcuts import render,redirect, get_object_or_404
from .models import Task,Team,Comment
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, TaskForm,CommentForm
from django.contrib.auth.models import User
@login_required
def home(request):
        if request.method=="POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task=form.save(commit=False)
                task.task_creator = request.user
                task.save()
                return redirect('home')
        else:
            form = TaskForm()
            users = User.objects.exclude(username=request.user.username)
            try:
                tasks = Task.objects.filter(task_creator=request.user)
                Team.add_member(request.user,request.user,tasks)
            except Task.DoesNotExist:
                tasks=None
            try:
                    team = Team.objects.get(team_creator=request.user)
                    members=team.team_member.exclude(username=request.user.username)
                    tasks=team.member_task.all()
                    context={
                    'form':form,
                    'users':users,
                    'members':members,
                    'tasks':tasks
                    }
                    return render(request, 'djangoApp/home.html',context)
            except Team.DoesNotExist:
                    team = None
                    members=None
                    context={
                    'form':form,
                    'users':users,
                    'members':members
                    }
        return render(request, 'djangoApp/home.html',context)
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
             form=SignUpForm(request.POST)
             if form.is_valid():
                 user = form.save()
                 return redirect('home')
    else :
        form = SignUpForm()
    return render(request,'registration/signup.html',{'form':form})
@login_required
def change_member(request,operation,pk):
     new_member= User.objects.get(pk=pk)
     try:
         tasks = Task.objects.filter(task_creator=new_member)
     except Task.DoesNotExist:
         tasks=None
     if operation=='add':
         Team.add_member(request.user,new_member,tasks)
     elif operation == 'remove':
         Team.remove_member(request.user,new_member,tasks)
     return redirect('team')
@login_required
def team(request):
    users = User.objects.exclude(username=request.user.username)
    try:
            team = Team.objects.get(team_creator=request.user)
            members=team.team_member.exclude(username=request.user.username)
            context={
            'users':users,
            'members':members
            }
    except Team.DoesNotExist:
            team = None
            members=None
            context={
            'users':users,
            'members':members
            }
    return render(request,'djangoApp/team.html',context)
@login_required
def add_comment(request,pk):
     task=get_object_or_404(Task, pk=pk)
     if request.method=="POST":
                  cform=CommentForm(request.POST)
                  if cform.is_valid():
                      comment = cform.save(commit=False)
                      comment.usr=request.user
                      comment.task =task
                      comment.save()
                      return redirect('add_comment',pk=pk)
     else:
         cform = CommentForm()
         cmnts = Comment.objects.filter(task=task)
         context={'form':cform,
                   'task':task,
                   'cmnts':cmnts}
         return render(request,'djangoApp/addcomment.html',context)
