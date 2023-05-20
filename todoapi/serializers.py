from rest_framework import serializers
from todos.models import Todo_Entity

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_Entity
        fields = '__all__'