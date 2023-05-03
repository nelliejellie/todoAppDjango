from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .forms import UserForm
from .models import Todo_Entity

# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def todos_list(request):

    form = UserForm()
    context = {'todos': Todo_Entity.objects.all(),'form':form}
    return render(request, 'todos.html', context)

def todo_form(request):
    if request.method == "Get":
        form = TodoForm()
        return render(request, 'todo_form.html', {'form':form})
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
def todo_delete(request):
    return

def todo_update(request):
    return