from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'todos'
#urlconfig
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.todos_list, name='todo_list'),
    path('form/', views.todo_form, name='todo_form'),
    path('accounts/login/', views.MyLoginView.as_view(), name='login'),
    path('accounts/logout/', views.MyLogoutView.as_view(), name='logout')
]