from rest_framework.serializers import ModelSerializer

from .models import Todo


class ForListView(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
