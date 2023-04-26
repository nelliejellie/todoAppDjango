from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoForm
from .forms import UserForm

# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def todos_list(request):
    form = UserForm()
    return render(request, 'todos.html', {'form':form})

def todo_form(request):
    form = TodoForm()
    return render(request, 'todo_form.html', {'form':form})

def todo_delete(request):
    return

def todo_update(request):
    return