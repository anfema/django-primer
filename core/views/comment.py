from rest_framework import permissions, viewsets

from core.models import TicketComment
from core.serializers import TicketCommentSerializer


class TicketCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketCommentSerializer
    queryset = TicketComment.objects.all().order_by("-created_at", "-updated_at")
