from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.conf import settings
import os
import logging
from backend.forms import ContactForm
from backend.models import Slider

logger = logging.getLogger(__name__)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')

            email_message = EmailMessage(
                subject=f'Message from {name}',
                body=message,
                from_email=email,
                to=[settings.DEFAULT_FROM_EMAIL],
                headers={'Reply-To': email}
            )

            if attachment:
                email_message.attach(attachment.name, attachment.read(), attachment.content_type)

            email_message.send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def get_images(request):
    image_folder = os.path.join(settings.BASE_DIR, 'backend/static/images')
    images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    images = [os.path.join('static/images', image) for image in images]
    sliders = Slider.objects.all()
    # sliders = Slider.objects.first()
    return render(request, 'gallery.html', {'sliders': sliders, 'images': images})


def index(request):
    image_folder = os.path.join(settings.BASE_DIR, 'backend/static/images')
    images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    images = [{'path': os.path.join('static/images', image), 'name': os.path.splitext(image)[0]} for image in images]
    return render(request, "index.html", {'images': images})
