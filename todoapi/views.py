from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from todos.models import Todo_Entity
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
def get_todos(request):
    if request.method == "GET":
        todos = Todo_Entity.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse({'todos':serializer.data})
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        serializer.initial_data['createdAt'] = timezone.now()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_todos(request):
    if request.method == 'POST':
        serializer = TodoSerializer(Todo_Entity, data=request.data)
        print(serializer)
        serializer.initial_data['createdAt'] = timezone.now()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def put_and_delete_todos(request, id):
    try:
        todo =Todo_Entity.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return  Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({"message":"deleted successfully"},status=status.HTTP_204_NO_CONTENT)
