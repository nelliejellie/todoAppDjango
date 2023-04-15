from django.urls import path
from . import views

#urlconfig
urlpatterns = [
    path('hello/', views.say_hello),
    path('', views.todos_list)
]