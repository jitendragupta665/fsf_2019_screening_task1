from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task,Comment


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description','assignee','status',)
class CommentForm(forms.ModelForm):
     first_name = forms.TextInput(attrs={'rows':4, 'cols':15})
     class Meta:
         model= Comment
         fields=('comment',)
