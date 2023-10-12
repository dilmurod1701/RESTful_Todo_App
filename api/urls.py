from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.List.as_view(), name='all'),
    path('api/<int:id>', views.Detail.as_view(), name='detail'),
    path('api/new', views.Create.as_view(), name='create'),
    path('api/<int:id>/delete', views.Delete.as_view(), name='delete'),
    path('api/<int:id>/update', views.Update.as_view(), name='update'),
]
