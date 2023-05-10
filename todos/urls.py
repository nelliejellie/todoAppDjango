from django.urls import path
from . import views

app_name = 'todos'
#urlconfig
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.todos_list, name='todo_list'),
    path('form/', views.todo_form, name='todo_form'),
]