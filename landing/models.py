from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name


class LandingContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    schedule = models.TextField()
    testimonials = models.TextField()
    faq = models.TextField()

    def __str__(self):
        return self.title