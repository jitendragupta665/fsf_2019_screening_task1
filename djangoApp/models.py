from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    task_creator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    assignee = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Team(models.Model):
    team_member = models.ManyToManyField(settings.AUTH_USER_MODEL)
    team_creator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='owner',null=True)
    @classmethod
    def add_member(cls,team_creator,new_member):
        team,create=cls.objects.ger_or_create(team_creator=team_creator)
        team.team_member.add(new_member)
    @classmethod
    def remove_member(cls,team_creator,member):
        team,create=cls.objects.ger_or_create(team_creator=team_creator)
        team.team_member.remove(new_member)
