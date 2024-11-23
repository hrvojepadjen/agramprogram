from rest_framework.routers import DefaultRouter
from .api_views import OrganizerViewSet, OrganizerTypeViewSet

router = DefaultRouter()
router.register(r'organizer-types', OrganizerTypeViewSet, basename='organizer-type')
router.register(r'organizers', OrganizerViewSet, basename='organizer')

urlpatterns = router.urls
