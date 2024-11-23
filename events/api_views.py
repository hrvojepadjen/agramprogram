from rest_framework import viewsets
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
