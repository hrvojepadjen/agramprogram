import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    """
    Filters for the Event model.
    """
    start_date = django_filters.DateFilter(
        field_name="start_datetime",
        lookup_expr="gte",
        label="Start Date (From)"
    )
    end_date = django_filters.DateFilter(
        field_name="end_datetime",
        lookup_expr="lte",
        label="End Date (To)"
    )
    price = django_filters.RangeFilter(
        field_name="price",
        label="Price Range"
    )

    class Meta:
        model = Event
        fields = [
            "organizer",
            "target_age_groups",
            "event_type",
            "start_date",
            "end_date",
            "price"
        ]
