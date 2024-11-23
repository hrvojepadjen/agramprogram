from rest_framework import viewsets
from .models import Organizer, OrganizerType
from .serializers import OrganizerSerializer, OrganizerTypeSerializer

class OrganizerTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for OrganizerType.
    """
    queryset = OrganizerType.objects.all()
    serializer_class = OrganizerTypeSerializer

class OrganizerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for Organizer.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer