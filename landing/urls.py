from django.urls import path
from .views import landing_page, thank_you

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('thank_you/', thank_you, name='thank_you'),
]
