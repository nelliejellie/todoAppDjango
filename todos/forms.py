from django import forms
from .models import Todo_Entity
from .models import userProfile

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_Entity
        fields = {'title','description','createdAt','user'}

    def __init__(self, *args, **kwargs):
        super(TodoForm,self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Select User"

class UserForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# use tuple to provide fields if not all