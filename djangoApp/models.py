from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    task_creator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    assignee = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
class Team(models.Model):
    team_member = models.ManyToManyField(settings.AUTH_USER_MODEL)
    team_creator=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='own',on_delete=models.CASCADE,null=True)
    member_task = models.ManyToManyField(Task)
    @classmethod
    def add_member(cls,team_creator,new_member,tasks):
        team,create=cls.objects.get_or_create(team_creator=team_creator)
        team.team_member.add(new_member)
        for task in tasks:
           team.member_task.add(task)
    @classmethod
    def remove_member(cls,team_creator,new_member,tasks):
        team,created =cls.objects.get_or_create(team_creator=team_creator)
        team.team_member.remove(new_member)
        for task in tasks:
           team.member_task.remove(task)
class Comment(models.Model):
        task = models.ForeignKey('djangoApp.Task', on_delete=models.CASCADE, related_name='comments')
        usr=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
        comment = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
