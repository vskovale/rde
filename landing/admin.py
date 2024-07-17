from django.contrib import admin
from .models import Contact, LandingContent

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'comments')
    search_fields = ('name', 'email')

@admin.register(LandingContent)
class LandingContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title', 'date', 'location')
