from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Slide(models.Model):
    slider = models.ForeignKey(Slider, related_name='slides', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='slides/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
