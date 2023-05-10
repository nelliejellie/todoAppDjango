from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .forms import UserForm
from .models import Todo_Entity

# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def todos_list(request):
    if request.method == "GET":
        form = UserForm()
        context = {'todos': Todo_Entity.objects.all(),'form':form}
        return render(request, 'todos.html', context)
    else:
        status = request.POST.get('status')
        if status is not None:
            my_object = Todo_Entity.objects.get(id=status)
            if my_object.done == False:
                my_object.done = True
                my_object.save()
                return redirect('/')
            else:
                my_object.done = False
                my_object.save()
                return redirect('/')
        form = UserForm((request.POST))
        if form.is_valid():
            form.save()
        return redirect('/')


def todo_form(request):
    if request.method == "GET":
        form = TodoForm()
        return render(request, 'todo_form.html', {'form':form})
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
def todo_delete(request):
    return

def todo_update_status(request):
    if request.method == "POST":
        status = request.POST.get('status')
        print(status + 1)