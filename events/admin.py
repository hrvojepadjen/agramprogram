from django.contrib import admin
from .models import EventType, Category, AgeGroup, Event


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "event_type",
        "organizer",
        "location",
        "start_datetime",
        "end_datetime",
        "price"
    )
    list_filter = (
        "event_type",
        "categories",
        "organizer",
        "target_age_groups",
        "registration_required"
    )
    search_fields = ("name", "description", "location")
    filter_horizontal = ("categories", "target_age_groups")
