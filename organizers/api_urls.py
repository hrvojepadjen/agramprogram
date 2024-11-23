from rest_framework.routers import DefaultRouter
from .api_views import (
    OrganizerViewSet,
    OrganizerTypeViewSet,
    CityDistrictViewSet
)

router = DefaultRouter()
router.register(r'organizer-types', OrganizerTypeViewSet, basename='organizer-type')
router.register(r'organizers', OrganizerViewSet, basename='organizer')
router.register(r'districts', CityDistrictViewSet, basename='districts')

urlpatterns = router.urls
