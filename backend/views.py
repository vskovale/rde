from django.shortcuts import render
from django.conf import settings
import os


def get_images(request):
    image_folder = os.path.join(settings.BASE_DIR, 'backend/static/images')
    images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    images = [os.path.join('static/images', image) for image in images]
    return render(request, 'gallery.html', {'images': images})


def index(request):
    return render(request, "index.html")
