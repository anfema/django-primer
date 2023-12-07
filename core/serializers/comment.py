from rest_framework import serializers

from core.models import TicketComment


class TicketCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketComment
        fields = "__all__"
