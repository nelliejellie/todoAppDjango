from django.urls import path
from . import views

app_name = 'todoapi'
urlpatterns = [
    path('todos/', views.get_todos),
    path('todos/create/', views.post_todos),
    path('todos/<int:id>', views.put_and_delete_todos)
]