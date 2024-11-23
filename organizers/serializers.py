from rest_framework import serializers
from .models import Organizer, OrganizerType


class OrganizerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizerType
        fields = ['id', 'name']  # Include relevant fields


class OrganizerSerializer(serializers.ModelSerializer):
    organizer_type = OrganizerTypeSerializer(read_only=True)
    organizer_type_id = serializers.PrimaryKeyRelatedField(
        source='organizer_type', queryset=OrganizerType.objects.all(), write_only=True
    )

    class Meta:
        model = Organizer
        fields = [
            'id', 'name', 'organizer_type', 'organizer_type_id', 'location',
            'contact_email', 'has_parking', 'pet_friendly',
            'wheelchair_accessible_entry', 'wheelchair_accessible_wc',
            'logo_url', 'user'
        ]
