from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def todos_list(request):
    return render(request, 'todos.html', {'name':'Dubem'})

def todo_form(request):
    return render(request, 'todo_form.html')

def todo_delete(request):
    return

def todo_update(request):
    return