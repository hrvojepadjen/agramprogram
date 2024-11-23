from rest_framework import viewsets
from .models import Organizer, OrganizerType, CityDistrict
from .serializers import (
    OrganizerSerializer,
    OrganizerTypeSerializer,
    CityDistrictSerializer,
)

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

class CityDistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for Organizer.
    """
    queryset = CityDistrict.objects.all()
    serializer_class = CityDistrictSerializer
