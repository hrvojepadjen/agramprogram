# django imports
from django.urls import path

# 3rd party imports
from rest_framework.routers import DefaultRouter

# local imports
from .api_views import (
    EventViewSet,
    EventTypeViewSet,
    CategoryViewSet,
    AgeGroupViewSet,
    CarouselAPIView,
)

router = DefaultRouter()
router.register(r'event-types', EventTypeViewSet, basename='event-type')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'age-groups', AgeGroupViewSet, basename='age-group')
router.register(r'events', EventViewSet, basename='event')

urlpatterns = router.urls

urlpatterns = router.urls + [
    path('carousel/', CarouselAPIView.as_view(), name='blank-api'),  # Add the CarouselAPIView
]
