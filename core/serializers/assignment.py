from rest_framework import serializers

from core.models import TicketAssigment


class TicketAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketAssigment
        fields = "__all__"
