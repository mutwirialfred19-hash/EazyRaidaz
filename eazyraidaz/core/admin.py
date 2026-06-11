from django.contrib import admin
from .models import RiderApplication, ContactMessage


@admin.register(RiderApplication)
class RiderApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'location', 'status', 'applied_at']
    list_filter = ['status', 'applied_at']
    search_fields = ['full_name', 'phone', 'email']
    list_editable = ['status']
    readonly_fields = ['applied_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'subject', 'sent_at', 'is_read']
    list_filter = ['is_read', 'sent_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['sent_at']
