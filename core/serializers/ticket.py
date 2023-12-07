from rest_framework import serializers

from core.models import Ticket


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "url",
            "title",
            "description",
            "current_lane",
            "created_at",
            "updated_at",
            "created_by",
            "comments",
            "assignments",
        ]
