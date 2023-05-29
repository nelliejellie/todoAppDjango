from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TodoForm
from .forms import UserForm
from .models import Todo_Entity
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

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
def todo_delete(request, id):
    myObject =get_object_or_404(Todo_Entity, id=id)
    myObject.delete()
    return redirect('/')

def todo_update_status(request):
    if request.method == "POST":
        status = request.POST.get('status')
        print(status + 1)
        return HttpResponse('yeah')

class MyLoginView(LoginView):
    template_name = 'registration/login.html'

class MyLogoutView(LogoutView):
    next_page = ('/')