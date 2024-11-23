from django.contrib import admin
from .models import OrganizerType, Organizer


@admin.register(OrganizerType)
class OrganizerTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ("name", "organizer_type", "location", "contact_email", "has_parking", "pet_friendly", "tag_list")
    list_filter = ("organizer_type", "has_parking", "pet_friendly", "wheelchair_accessible_entry", "wheelchair_accessible_wc")
    search_fields = ("name", "location", "contact_email")
    readonly_fields = ("logo_url",)

    fieldsets = (
        (None, {'fields': ('tags',)}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
