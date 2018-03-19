from django.urls import path, re_path
from . import views

from django.views.generic import DetailView
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('single/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='post_detail'),
    path('upload/',views.UploadView.as_view(), name='post_create'),
    path('delete/<int:pk>/',views.PhotoDeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/',views.PhotoUpdateView.as_view(), name='post_update'),
]