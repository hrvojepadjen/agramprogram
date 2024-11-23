# django imports
from django.utils.timezone import now

# 3rd party imports
from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# python imports
from datetime import datetime, timedelta

# local imports
from .models import Event, EventType, Category, AgeGroup
from .serializers import EventSerializer, EventTypeSerializer, CategorySerializer, AgeGroupSerializer


class EventTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for EventType.
    """
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AgeGroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for AgeGroup.
    """
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API endpoint for Event.
    """
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name',
        'description',
        'description_en',
        'city_district__name',
        'organizer__name',
        'event_type__name',
        'categories__name',
    ]

    def get_next_week_dates(self):
        today = datetime.now()
        # Calculate the start of the next week (Monday)
        days_until_next_monday = (7 - today.weekday()) % 7 + 1
        next_week_start = today + timedelta(days=days_until_next_monday)
        next_week_start = next_week_start.replace(hour=0, minute=0, second=0, microsecond=0)

        # Calculate the end of the next week (Sunday)
        next_week_end = next_week_start + timedelta(days=6)
        next_week_end = next_week_end.replace(hour=23, minute=59, second=59, microsecond=999999)

        return next_week_start, next_week_end

    def get_this_weekend_dates(self):
        today = datetime.now()
        # Calculate the start of Saturday (this weekend)
        days_until_saturday = (5 - today.weekday()) % 7  # Saturday is day 5 (Monday=0)
        saturday_start = today + timedelta(days=days_until_saturday)
        saturday_start = saturday_start.replace(hour=0, minute=0, second=0, microsecond=0)

        # Calculate the end of Sunday (this weekend)
        sunday_end = saturday_start + timedelta(days=1)
        sunday_end = sunday_end.replace(hour=23, minute=59, second=59, microsecond=999999)

        return saturday_start, sunday_end

    def get_queryset(self):
        queryset = Event.objects.all()

        # datum
        date = self.request.query_params.get('date')

        if date is not None:
            if date == "sutra":
                tomorrow = now().date() + timedelta(days=1)
                queryset = queryset.filter(
                    start_datetime__date=tomorrow
                )

            if date == "danas":
                today = now().date()
                queryset = queryset.filter(
                    start_datetime__date=today
                )

            if date == "iduci_tjedan":
                next_week_start, next_week_end = self.get_next_week_dates()

                queryset = queryset.filter(
                    start_datetime__gte=next_week_start,
                    start_datetime__lte=next_week_end,
                )

            if date == "ovaj_vikend":
                saturday_start, sunday_end = self.get_this_weekend_dates()

                queryset = queryset.filter(
                    start_datetime__gte=saturday_start,
                    start_datetime__lte=sunday_end,
                )

            if date == "range":
                from_date_str = self.request.query_params.get('from_date')
                to_date_str = self.request.query_params.get('to_date')

                if from_date and to_date:
                    from_date = datetime.fromisoformat(from_date_str)
                    to_date = datetime.fromisoformat(to_date_str)

                    events = Event.objects.filter(
                        start_datetime__gte=from_date,
                        start_datetime__lte=to_date,
                    )

        # kvart
        district_id = self.request.query_params.get('district')

        if district_id is not None:
            queryset = queryset.filter(city_district__id=district_id)

        # vrsta događanja
        event_type_id = self.request.query_params.get('event_type')

        if event_type_id is not None:
            queryset = queryset.filter(event_type__id=event_type_id)

        # kategorija
        category_id = self.request.query_params.get('category')

        if category_id is not None:
            queryset = queryset.filter(categories__id=category_id)

        # cijena
        price = self.request.query_params.get('price')

        if price is not None:
            if price == "besplatno":
                queryset = queryset.filter(price=0)
            elif price == "do_10":
                queryset = queryset.filter(price__lte=10)
            elif price == "do_20":
                queryset = queryset.filter(price__lte=20)
            elif price == "iznad_20":
                queryset = queryset.filter(price__gte=20)

        return queryset


class CarouselAPIView(APIView):
    """
    An API view for carousel.
    """
    queryset = Event.objects.all()
    allowed_methods = ['GET']

    def get(self, request, *args, **kwargs):
        # create data for carousel no. 1 - featured events
        featured_events = self.queryset.filter(featured=True)
        featured_serializer = EventSerializer(featured_events, many=True)

        # create data for carousel no. 2 - today's events
        today = now().date()
        events_today = self.queryset.filter(
            start_datetime__date=today
        )
        events_today_serializer = EventSerializer(events_today, many=True)

        # create data for carousel no. 3 - tomorrow's events
        tomorrow = now().date() + timedelta(days=1)
        events_tomorrow = self.queryset.filter(
            start_datetime__date=tomorrow
        )
        events_tomorrow_serializer = EventSerializer(
            events_tomorrow,
            many=True
        )

        # add data
        data_total = {
            "carousel_1_data": featured_serializer.data,
            "carousel_2_data": events_today_serializer.data,
            "carousel_3_data": events_tomorrow_serializer.data,
        }

        return Response(
            data_total,
            status=status.HTTP_200_OK
        )
