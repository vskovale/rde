from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.get_images, name='get_images'),
    path('', views.index),
]
