from rest_framework import serializers

from core.models import Swimlane


class SwimlaneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Swimlane
        fields = ["url", "name", "description", "tickets"]
