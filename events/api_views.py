# 3rd party imports
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response

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
    queryset = Event.objects.all()
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
