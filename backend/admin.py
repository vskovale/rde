from django.contrib import admin
from .models import Slider, Slide

class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1

class SliderAdmin(admin.ModelAdmin):
    inlines = [SlideInline]

admin.site.register(Slider, SliderAdmin)
