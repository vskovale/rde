import os

from django.db import models

def get_image_path(instance, filename):
    return os.path.join('slides', filename)

class Slider(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Slide(models.Model):
    slider = models.ForeignKey(Slider, related_name='slides', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_path)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(default='')

    def __str__(self):
        return self.title
