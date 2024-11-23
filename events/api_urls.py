from rest_framework.routers import DefaultRouter
from .api_views import EventViewSet, EventTypeViewSet, CategoryViewSet, AgeGroupViewSet

router = DefaultRouter()
router.register(r'event-types', EventTypeViewSet, basename='event-type')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'age-groups', AgeGroupViewSet, basename='age-group')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls
