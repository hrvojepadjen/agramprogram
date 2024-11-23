from rest_framework import serializers
from .models import Event, EventType, Category, AgeGroup

from taggit.serializers import TagListSerializerField, TaggitSerializer

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'name']  # Include relevant fields

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Include relevant fields

class AgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroup
        fields = ['id', 'name']  # Include relevant fields

class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    event_type = EventTypeSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    target_age_groups = AgeGroupSerializer(many=True, read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Event
        fields = [
            'id', 'name', 'description', 'description_en', 'event_type',
            'categories', 'organizer', 'location', 'start_datetime',
            'end_datetime', 'target_age_groups', 'price', 'tickets_available',
            'registration_required', 'registration_deadline', 'created_at',
            'updated_at', 'tags'
        ]
