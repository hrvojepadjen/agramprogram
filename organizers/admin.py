from django.contrib import admin
from .models import OrganizerType, Organizer


@admin.register(OrganizerType)
class OrganizerTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ("name", "organizer_type", "location", "contact_email", "has_parking", "pet_friendly")
    list_filter = ("organizer_type", "has_parking", "pet_friendly", "wheelchair_accessible_entry", "wheelchair_accessible_wc")
    search_fields = ("name", "location", "contact_email")
    readonly_fields = ("logo_url",)
