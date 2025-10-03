from django.contrib import admin
from .models import ContactMessage, Gift, Reservation


# Register your models here.

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_reserved', 'reserved_by')
    search_fields = ('name', 'description')
    list_filter = ('is_reserved',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'gift', 'reserved_at')
    search_fields = ('user__username', 'gift__name')
    list_filter = ('reserved_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
