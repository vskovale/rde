from django.shortcuts import render
from django.conf import settings
import os
import logging
from backend.models import Slider

logger = logging.getLogger(__name__)


def get_images(request):
    image_folder = os.path.join(settings.BASE_DIR, 'backend/static/images')
    images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    images = [os.path.join('static/images', image) for image in images]
    sliders = Slider.objects.all()
    # sliders = Slider.objects.first()
    return render(request, 'gallery.html', {'sliders': sliders, 'images': images})


def index(request):
    return render(request, "index.html")
