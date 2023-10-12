from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .models import Todo
from .serializers import TodoSerializer, ForListView

# Create your views here.


class List(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ForListView


class Detail(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"


class Create(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Delete(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"


class Update(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"
