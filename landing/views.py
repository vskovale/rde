from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import LandingContent


def landing_page(request):
    content = LandingContent.objects.last()  # Получаем первый объект контента
    if content:
        schedule = content.schedule.split('\n')
        testimonials = content.testimonials.split('\n')
        faq = content.faq.split('\n')
    else:
        schedule = []
        testimonials = []
        faq = []

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'content': content,
        'schedule': schedule,
        'testimonials': testimonials,
        'faq': faq,
    }
    return render(request, 'landing_page.html', context)


def thank_you(request):
    return render(request, 'thank_you.html')
