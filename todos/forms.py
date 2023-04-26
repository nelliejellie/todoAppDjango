from django import forms
from .models import Todo_Entity
from .models import userProfile

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_Entity
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = '__all__'

# use tuple to provide fields if not all